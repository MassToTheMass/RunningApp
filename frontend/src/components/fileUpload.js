import { useState } from "react";

function FileUpload() {
    const [file, setFile] = useState(null);
      
    const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    await fetch('http://localhost:5000/api/upload', {
      method: 'POST',
      body: formData,
    });

    alert('File uploaded successfully!');
  };

  return (
    <div className="App">
		<h1>Upload a Run</h1>

		<input type="file" onChange={(e) => setFile(e.target.files[0])} />

		<button onClick={handleUpload}>Upload</button>
    </div>
  );
}

export default FileUpload;