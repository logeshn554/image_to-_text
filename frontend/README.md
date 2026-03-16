# Image Caption Generator Frontend

React UI for generating text captions from images using BLIP AI model.

## Features

- **Drag & Drop Upload** - Easy image upload with preview
- **Caption Generation** - AI-powered text generation from images
- **Error Handling** - Clear feedback on failures
- **Loading States** - Visual indicators during processing
- **Dark Mode** - Automatic theme support
- **Responsive Design** - Works on mobile, tablet, desktop

## Components

| Component | Purpose |
|-----------|---------|
| `Header.tsx` | Page header with title |
| `Footer.tsx` | Footer information |
| `UploadForm.tsx` | Drag-drop file upload |
| `LoadingSpinner.tsx` | Loading indicator |
| `ErrorMessage.tsx` | Error notifications |

## Development

```bash
npm install       # Install dependencies
npm run dev       # Start dev server (http://localhost:5176)
npm run build     # Build for production
npm run lint      # Run ESLint
```

## Environment

Create `.env` file (copy from `.env.example`):

```
VITE_API_URL=http://localhost:8000
```

## Building

```bash
npm run build  # Creates dist/ folder
```

## Technologies

- React 19
- TypeScript 5.9
- Vite 8.0
- CSS3 (no Tailwind)

    extends: [
      // Other configs...

      // Remove tseslint.configs.recommended and replace with this
      tseslint.configs.recommendedTypeChecked,
      // Alternatively, use this for stricter rules
      tseslint.configs.strictTypeChecked,
      // Optionally, add this for stylistic rules
      tseslint.configs.stylisticTypeChecked,

      // Other configs...
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```

You can also install [eslint-plugin-react-x](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-x) and [eslint-plugin-react-dom](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-dom) for React-specific lint rules:

```js
// eslint.config.js
import reactX from 'eslint-plugin-react-x'
import reactDom from 'eslint-plugin-react-dom'

export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...
      // Enable lint rules for React
      reactX.configs['recommended-typescript'],
      // Enable lint rules for React DOM
      reactDom.configs.recommended,
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```
