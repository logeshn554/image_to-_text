export default function ErrorMessage({ 
  message, 
  onClose 
}: { 
  message: string | null
  onClose: () => void 
}) {
  if (!message) return null

  return (
    <div className="error-message">
      <div className="error-content">
        <span>❌ {message}</span>
        <button onClick={onClose} className="error-close">×</button>
      </div>
    </div>
  )
}
