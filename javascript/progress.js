const progressBar = document.getElementById('progressBar');
const slider = document.getElementById('slider');

slider.addEventListener('input', function () {
  const value = parseInt(this.value, 10);
  progressBar.style.width = value + '%';
  progressBar.textContent = value + '%';

  if (value < 30) {
    progressBar.style.backgroundColor = 'red';
  } else if (value < 70) {
    progressBar.style.backgroundColor = 'orange';
  } else {
    progressBar.style.backgroundColor = 'green';
  }
});
