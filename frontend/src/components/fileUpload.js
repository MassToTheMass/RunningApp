import { useRef, useState } from "react";

function FileUpload({ fetchRuns }) {
    const [file, setFile] = useState(null);
    const fileInputRef = useRef(null);

    const handleClick = () => {
        fileInputRef.current.click();
    };

    const handleFileChange = (e) => {
        const selectedFile = e.target.files[0];
        setFile(selectedFile);

      if (selectedFile) {
          uploadFile(selectedFile);
      }
    };

    const uploadFile = async (file) => {
    const formData = new FormData();
    formData.append('file', file);

    await fetch('http://localhost:5000/api/upload', {
      method: 'POST',
      body: formData,
    });

      fetchRuns();
    alert('File uploaded successfully!');
  };

  return (
    <div>
      <input type="file" ref={fileInputRef} style={{ display: "none" }} onChange={handleFileChange} />
      <button className="sidebarbutton" onClick={handleClick}>Upload</button>
    </div>
  );
}

export default FileUpload;