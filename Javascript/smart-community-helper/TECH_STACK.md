# 🛠️ Tech Stack Details

Here's the breakdown of everything I used to build this. Some choices I'm proud of, others... well, they work.

## Frontend Technologies

### React.js
- **Version**: 18.2.0+
- **Why**: Just works well, huge community, tons of resources
- **Key Features**: Hooks are awesome, component reusability is great
- **Use Cases**: UI components, state management (with Redux)

### Tailwind CSS
- **Version**: 3.3+
- **Why**: Writing CSS from scratch was taking forever
- **Key Features**: Utility classes save so much time, responsive design is easy
- **Use Cases**: Quick styling, responsive layouts, dark mode (planned)

### Material-UI (MUI)
- **Version**: 5.14+
- **Why**: Pre-built components for common stuff like forms and buttons
- **Key Features**: Lots of components out of the box, good docs
- **Use Cases**: Forms, dialogs, data tables, navigation

### Redux Toolkit
- **Version**: 1.9+
- **Why**: Tried Context API but got messy with complexity
- **Key Features**: Makes Redux way less painful than it used to be
- **Use Cases**: Global state, API calls, caching

### React Router
- **Version**: 6.16+
- **Why**: Standard routing solution, works well
- **Key Features**: Nested routes, lazy loading, protected routes
- **Use Cases**: Navigation, route protection

### Google Maps API
- **Version**: Latest
- **Why**: Tried other map libraries but Google's is most reliable
- **Key Features**: Interactive maps, geocoding, markers
- **Use Cases**: Marking issue locations, map view

**Note:** Watch your API usage, costs can add up.

## Backend Technologies

### Node.js
- **Version**: 18.x (using 18.17.0)
- **Why**: JavaScript everywhere is nice, npm ecosystem is huge
- **Key Features**: Non-blocking I/O, works well
- **Use Cases**: API server, real-time stuff

### Express.js
- **Version**: 4.18+
- **Why**: Simple, does what I need without getting in the way
- **Key Features**: Middleware support, routing is straightforward
- **Use Cases**: RESTful API, request handling

### MongoDB
- **Version**: 6.0+
- **Why**: Flexible schema, didn't want to deal with migrations
- **Key Features**: Documents are easy to work with, scaling is straightforward
- **Use Cases**: Store user data, issues, comments

### Mongoose
- **Version**: 7.5+
- **Why**: Easier than raw MongoDB queries
- **Key Features**: Schema definition, validation, relationships
- **Use Cases**: Data modeling, queries

### JWT (JSON Web Tokens)
- **Why**: Stateless auth is simpler than sessions
- **Key Features**: Works well, scalable
- **Use Cases**: User authentication, API auth

### bcrypt
- **Version**: 5.1+
- **Why**: Standard password hashing, everyone uses it
- **Key Features**: Secure hashing, async support
- **Use Cases**: Hash passwords

### OpenAI API
- **Why**: Best AI models available, good docs
- **Key Features**: GPT models, text analysis
- **Use Cases**: Issue categorization, solution generation

**Warning:** This gets expensive fast. Monitor your usage!

### Socket.io
- **Version**: 4.6+
- **Why**: Wanted real-time updates without too much hassle
- **Key Features**: WebSocket support, rooms, events
- **Use Cases**: Real-time updates, notifications

## DevOps & Tools

### Docker
- **Version**: Latest
- **Why**: Makes deployment easier, consistent environments
- **Key Features**: Containerization, isolation
- **Use Cases**: Development, production deployment

### Docker Compose
- **Version**: Latest
- **Why**: Easier than running multiple services manually
- **Key Features**: Multi-container apps, networking
- **Use Cases**: Local development, testing

### GitHub Actions
- **Why**: Free CI/CD, integrates well with GitHub
- **Key Features**: Automated testing, deployment workflows
- **Use Cases**: Run tests, deploy automatically

### Vercel
- **Why**: Easy frontend deployment, works great with React
- **Key Features**: Automatic deployments, edge network
- **Use Cases**: Host frontend, CI/CD

### Railway
- **Why**: Simple backend deployment, manages databases too
- **Key Features**: Easy deployment, automatic HTTPS
- **Use Cases**: Host backend API, MongoDB hosting

### MongoDB Atlas
- **Why**: Don't want to manage MongoDB myself
- **Key Features**: Managed service, backups, scaling
- **Use Cases**: Production database

## Development Tools

### ESLint
- **Version**: 8.50+
- **Why**: Catches bugs before runtime
- **Key Features**: Custom rules, auto-fix
- **Use Cases**: Code quality, consistency

### Prettier
- **Version**: 3.0+
- **Why**: No more arguing about code style
- **Key Features**: Auto-formatting, consistent style
- **Use Cases**: Code formatting

### Jest
- **Version**: 29.6+
- **Why**: Popular testing framework, good docs
- **Key Features**: Snapshot testing, mocking
- **Use Cases**: Unit tests, integration tests

### React Testing Library
- **Version**: 14.0+
- **Why**: Tests components from user perspective
- **Key Features**: User-centric testing, accessibility testing
- **Use Cases**: Component tests

### Postman
- **Why**: Easier than curl for testing APIs
- **Key Features**: Request testing, collections
- **Use Cases**: API testing, debugging

## Additional Tools

### Cloudinary
- **Why**: Don't want to deal with file storage
- **Key Features**: Upload, transformation, optimization
- **Use Cases**: Photo/video storage, image optimization

### Nodemailer
- **Version**: 6.9+
- **Why**: Sending emails from Node.js
- **Key Features**: SMTP support, attachments
- **Use Cases**: User notifications, system emails

### Express Validator
- **Version**: 7.0+
- **Why**: Input validation without writing custom code
- **Key Features**: Validation rules, sanitization
- **Use Cases**: Request validation

### Morgan
- **Version**: 1.10+
- **Why**: Logging HTTP requests for debugging
- **Key Features**: Log formats, custom tokens
- **Use Cases**: Request logging, debugging

### Helmet
- **Version**: 7.0+
- **Why**: Security headers, prevents common attacks
- **Key Features**: Security headers, XSS protection
- **Use Cases**: Security headers

## Environment & Dependencies

### Required Node.js Packages
```json
{
  "dependencies": {
    "express": "^4.18.2",
    "mongoose": "^7.5.0",
    "bcrypt": "^5.1.1",
    "jsonwebtoken": "^9.0.2",
    "socket.io": "^4.6.1",
    "openai": "^4.10.0",
    "dotenv": "^16.3.1",
    "cors": "^2.8.5",
    "helmet": "^7.0.0",
    "express-validator": "^7.0.1",
    "morgan": "^1.10.1",
    "cloudinary": "^1.40.0",
    "nodemailer": "^6.9.7"
  },
  "devDependencies": {
    "nodemon": "^3.0.1",
    "jest": "^29.6.2",
    "supertest": "^6.3.3",
    "eslint": "^8.50.0",
    "prettier": "^3.0.3"
  }
}
```

### Required React Packages
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.16.0",
    "@reduxjs/toolkit": "^1.9.7",
    "react-redux": "^8.1.3",
    "@mui/material": "^5.14.18",
    "@mui/icons-material": "^5.14.18",
    "axios": "^1.5.1",
    "socket.io-client": "^4.6.1",
    "@googlemaps/js-api-loader": "^1.16.2"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.0",
    "vite": "^4.5.0",
    "eslint": "^8.50.0",
    "prettier": "^3.0.3",
    "@testing-library/react": "^14.0.0",
    "@testing-library/jest-dom": "^6.1.4"
  }
}
```

## Database Schema Overview

### Users Collection
- User credentials (email, hashed password)
- Profile information (name, avatar, bio)
- Activity history (issues reported, comments made)
- Preferences (notifications, privacy settings)

### Issues Collection
- Issue details (title, description, category)
- Location data (coordinates, address)
- Status tracking (open, in progress, resolved)
- Attachments (photos, videos)
- Priority level
- Timestamps

### Comments Collection
- Comment content
- User references
- Timestamps
- Thread relationships
- Likes/reactions

### Categories Collection
- Category definitions
- AI training data
- Priority mappings
- Department assignments

## API Architecture

### RESTful Endpoints
- `/api/auth` - Authentication routes (register, login, logout)
- `/api/users` - User management (get profile, update profile)
- `/api/issues` - Issue operations (CRUD)
- `/api/comments` - Comment system (add, edit, delete)
- `/api/categories` - Category management
- `/api/admin` - Admin operations (moderation, analytics)

### Real-time Events
- `issue:created` - New issue posted
- `issue:updated` - Issue status changed
- `comment:added` - New comment posted
- `notification:new` - New notification

---

That's the tech stack! Pretty standard choices, but they work well together.

