import { useState } from 'react'
import Header from './components/Header'
import UploadForm from './components/UploadForm'
import LoadingSpinner from './components/LoadingSpinner'
import ErrorMessage from './components/ErrorMessage'
import './App.css'

export default function App() {
  const [caption, setCaption] = useState<string | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const backend = import.meta.env.VITE_API_URL || 'http://localhost:8000'

  async function generateCaption(file: File) {
    setLoading(true)
    setError(null)
    setCaption(null)
    try {
      const form = new FormData()
      form.append('file', file)
      const res = await fetch(`${backend}/generate-caption`, { method: 'POST', body: form })
      if (!res.ok) {
        throw new Error(`Generation failed: HTTP ${res.status}`)
      }
      const data = await res.json()
      setCaption(data.caption)
    } catch (err) {
      const msg = err instanceof Error ? err.message : 'Caption generation failed'
      setError(msg)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <Header />

      <div className="content">
        <ErrorMessage message={error} onClose={() => setError(null)} />

        <div className="upload-section">
          <h2 className="section-title">Upload Image</h2>
          <UploadForm onSearch={generateCaption} uploading={loading} />
        </div>

        {loading && <LoadingSpinner message="Generating caption..." />}

        {caption && (
          <div className="results-section">
            <h2 className="section-title">Caption</h2>
            <div className="caption-box">
              {caption}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}


