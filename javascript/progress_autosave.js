document.addEventListener("DOMContentLoaded", () => {
  const progressBar = document.getElementById("progressBar");
  const courseId = parseInt(window.location.pathname.split("/")[2], 10); // /kurs/<id>/lernen

  let lastSentProgress = 0;

  function updateVisualProgress(percent) {
    progressBar.style.width = percent + "%";
    progressBar.textContent = percent + "%";

    if (percent < 30) {
      progressBar.style.backgroundColor = "red";
    } else if (percent < 70) {
      progressBar.style.backgroundColor = "orange";
    } else {
      progressBar.style.backgroundColor = "green";
    }
  }

  function sendProgress(progress) {
    if (Math.abs(progress - lastSentProgress) >= 5) {  // nur bei >5% Änderung senden
      lastSentProgress = progress;
      fetch(`/api/progress/${courseId}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ progress })
      });
    }
  }

  function trackLocalVideo(videoEl) {
    videoEl.addEventListener("timeupdate", () => {
      const percent = Math.floor((videoEl.currentTime / videoEl.duration) * 100);
      if (!isNaN(percent) && percent <= 100) {
        updateVisualProgress(percent);
        sendProgress(percent);
      }
    });
  }

  function trackYouTubeVideo() {
    const iframe = document.querySelector("iframe");
    if (!iframe) return;

    const player = new YT.Player(iframe, {
      events: {
        onReady: () => {
          setInterval(() => {
            const duration = player.getDuration();
            const current = player.getCurrentTime();
            if (duration > 0) {
              const percent = Math.floor((current / duration) * 100);
              updateVisualProgress(percent);
              sendProgress(percent);
            }
          }, 4000);
        }
      }
    });
  }

  // Initialisieren
  const video = document.querySelector("video");
  if (video) {
    trackLocalVideo(video);
  } else if (typeof YT !== "undefined") {
    trackYouTubeVideo();
  } else {
    // YouTube API laden
    const tag = document.createElement("script");
    tag.src = "https://www.youtube.com/iframe_api";
    document.body.appendChild(tag);
    window.onYouTubeIframeAPIReady = trackYouTubeVideo;
  }
});
