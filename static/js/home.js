function updateFileName() {
    const fileInput = document.getElementById('fileInput');
    const fileNameSpan = document.getElementById('fileName');
    const files = fileInput.files;

    if (files.length > 0) {
      fileNameSpan.textContent = files[0].name;
    } else {
      fileNameSpan.textContent = '';
    }
  }


