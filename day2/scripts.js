async function sendData(data, url) {
  try {
      const response = await fetch(url, {
          method: 'POST',
          body: data
      });

      const result = await response.json();
      console.log(result);
  } catch (error) {
      console.error(error);
  }
}

document.getElementById('form').addEventListener('submit', function (e) {
  e.preventDefault();
  var data = new FormData(this);
  sendData(data, 'api_php.php');
});
