import { useState } from 'react'

type Props = {
  onSearch: (file: File) => void
  uploading?: boolean
}

export default function UploadForm({ onSearch, uploading }: Props) {
  const [file, setFile] = useState<File | null>(null)
  const [dragActive, setDragActive] = useState(false)

  const handleDrag = (e: React.DragEvent) => {
    e.preventDefault()
    e.stopPropagation()
    setDragActive(e.type !== 'dragleave')
  }

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault()
    e.stopPropagation()
    setDragActive(false)
    const dropped = e.dataTransfer.files?.[0]
    if (dropped?.type.startsWith('image/')) {
      setFile(dropped)
    }
  }

  return (
    <>
      <div className={`drop-zone ${dragActive ? 'active' : ''}`} onDragEnter={handleDrag} onDragLeave={handleDrag} onDragOver={handleDrag} onDrop={handleDrop}>
        <input
          type="file"
          accept="image/*"
          onChange={e => setFile(e.target.files?.[0] ?? null)}
          className="file-input"
          id="file-input"
        />
        <label htmlFor="file-input" className="drop-label">
          {file ? (
            <>{file.name}</>
          ) : (
            <>
              <p className="drop-text">Drag and drop your image here</p>
              <p className="drop-subtext">or click to browse</p>
            </>
          )}
        </label>
      </div>

      {file && (
        <div className="preview-container">
          <img src={URL.createObjectURL(file)} alt="preview" className="preview-image" />
          <div className="preview-info">
            <p><strong>File:</strong> {file.name}</p>
            <p><strong>Size:</strong> {(file.size / 1024).toFixed(2)} KB</p>
          </div>
        </div>
      )}

      <div className="actions">
        <button 
          className="btn btn-primary" 
          onClick={() => file && onSearch(file)} 
          disabled={!file || uploading}
        >
          {uploading ? 'Generating...' : 'Generate Caption'}
        </button>
      </div>
    </>
  )
}
