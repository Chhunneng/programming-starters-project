# 🚀 Setup Instructions

Hey! So you want to run this locally? Cool! Here's my attempt at documenting the setup process. Fair warning - the first time I set this up, I ran into a bunch of random issues, so I'm trying to cover all the pitfalls here.

## 📋 Prerequisites

You'll need these installed before you start:

- **Node.js**: Version 18.x or higher ([Download](https://nodejs.org/)) - I'm using 18.17.0 but anything 18+ should work
- **MongoDB**: Version 6.0+ OR just use MongoDB Atlas (easier honestly) ([Download](https://www.mongodb.com/try/download/community))
- **Git**: Probably already have this, but just in case ([Download](https://git-scm.com/downloads))
- **Google Maps API Key**: Sign up at [Google Cloud Console](https://console.cloud.google.com/) - free tier is generous enough for testing
- **OpenAI API Key**: Sign up at [OpenAI Platform](https://platform.openai.com/) - warning: you'll need billing enabled. Sorry.

### Optional but Helpful
- **Docker**: Makes things easier if you're into that ([Download](https://www.docker.com/))
- **Postman**: For testing the API ([Download](https://www.postman.com/)) - or use curl, I'm not your boss

## 🔧 Installation Steps

### 1. Clone the Repository

```bash
# Clone the repository
git clone https://github.com/your-username/smart-community-helper.git

# Navigate to the project directory
cd smart-community-helper
```

### 2. Set Up Backend

```bash
# Navigate to backend directory
cd backend

# Install dependencies
npm install

# Create environment file
cp .env.example .env
```

### 3. Configure Environment Variables

Alright, this is where most people mess up. Open the `.env` file and fill in your actual values. DON'T commit this file to git! I learned that the hard way.

```env
# Server Configuration
PORT=5000
NODE_ENV=development

# MongoDB Configuration
# Use local MongoDB:
MONGODB_URI=mongodb://localhost:27017/smart-community-helper
# OR use MongoDB Atlas (recommended for first time):
# MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/smart-community-helper

# JWT Configuration
# Generate a random string for this - don't use something obvious
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
JWT_EXPIRE=7d

# OpenAI API Configuration
# Get this from https://platform.openai.com/api-keys
OPENAI_API_KEY=your-openai-api-key-here

# Google Maps API Configuration
# Get this from Google Cloud Console
GOOGLE_MAPS_API_KEY=your-google-maps-api-key-here

# Email Configuration (Optional - skip if you don't need email)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=your-app-password

# Cloudinary Configuration (Optional - image uploads won't work without this)
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

# Frontend URL (for CORS - change if your frontend runs on different port)
FRONTEND_URL=http://localhost:3000
```

**IMPORTANT:** If you skip Cloudinary setup, image uploads will fail. Just FYI.

### 4. Set Up Frontend

```bash
# Navigate to frontend directory
cd ../frontend

# Install dependencies
npm install

# Create environment file
cp .env.example .env
```

Edit the `.env` file in the frontend directory:

```env
# API Configuration
REACT_APP_API_URL=http://localhost:5000/api

# Google Maps API Key
REACT_APP_GOOGLE_MAPS_API_KEY=your-google-maps-api-key-here

# OpenAI Configuration (if needed on frontend)
REACT_APP_OPENAI_API_KEY=your-openai-api-key-here
```

### 5. Set Up MongoDB

Choose your poison:

#### Option A: Local MongoDB

```bash
# On macOS with Homebrew:
brew services start mongodb-community

# On Linux:
sudo systemctl start mongod

# On Windows:
# Just start MongoDB from Services or run mongod command
```

Pro tip: Local MongoDB can be annoying to manage. I'd go with Atlas if you're just testing.

#### Option B: MongoDB Atlas (Cloud) - RECOMMENDED

This is what I did:

1. Create an account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) - free tier is plenty
2. Create a new cluster (pick the free M0 tier)
3. Create a database user (remember the password!)
4. Whitelist your IP address (or just use 0.0.0.0/0 for development)
5. Get your connection string from "Connect" button
6. Paste it into `MONGODB_URI` in your `.env` file

Seriously, Atlas is way easier than dealing with local MongoDB.

### 6. Run Database Seeder (Optional but Helpful)

I included a seeder script to populate some test data so you can actually see the app working:

```bash
# Navigate to backend directory
cd backend

# Run seeder to populate initial data
npm run seed
```

This creates:
- Default admin user (email: admin@test.com, password: admin123 - CHANGE THIS!)
- Sample categories (Safety, Environment, etc.)
- A few sample issues to play with
- Some fake users

**Warning:** The seeder will wipe your database if you run it multiple times. Don't run it on production! 🙃

### 7. Start the Application

#### Start Backend Server

```bash
# Navigate to backend directory
cd backend

# Start development server
npm run dev

# The server will start on http://localhost:5000
```

#### Start Frontend Application

```bash
# Open a new terminal window
# Navigate to frontend directory
cd frontend

# Start development server
npm start

# The app will open on http://localhost:3000
```

## 🐳 Docker Setup (Alternative)

### Using Docker Compose

```bash
# From the project root directory
docker-compose up -d

# Check logs
docker-compose logs -f

# Stop containers
docker-compose down
```

### Environment Variables for Docker

Create a `.env` file in the project root:

```env
# MongoDB
MONGODB_URI=mongodb://mongo:27017/smart-community-helper

# JWT
JWT_SECRET=your-secret-key

# API Keys
OPENAI_API_KEY=your-openai-key
GOOGLE_MAPS_API_KEY=your-google-maps-key

# Ports
BACKEND_PORT=5000
FRONTEND_PORT=3000
```

## 🧪 Testing

### Run Backend Tests

```bash
cd backend

# Run all tests
npm test

# Run tests with coverage
npm run test:coverage

# Run tests in watch mode
npm run test:watch
```

### Run Frontend Tests

```bash
cd frontend

# Run all tests
npm test

# Run tests with coverage
npm run test:coverage
```

## 📝 API Documentation

### Access API Documentation

Once the backend server is running, visit:
- Swagger UI: `http://localhost:5000/api-docs`
- Postman Collection: Import `backend/postman-collection.json`

### Common API Endpoints

```
# Authentication
POST   /api/auth/register    - Register new user
POST   /api/auth/login        - Login user
GET    /api/auth/me           - Get current user

# Issues
GET    /api/issues            - Get all issues
POST   /api/issues            - Create new issue
GET    /api/issues/:id        - Get issue by ID
PUT    /api/issues/:id        - Update issue
DELETE /api/issues/:id        - Delete issue

# Comments
GET    /api/issues/:id/comments - Get comments for issue
POST   /api/issues/:id/comments - Add comment to issue
```

## 🔍 Verification

### Check Backend Setup

1. Visit `http://localhost:5000/api/health`
2. Should return: `{ "status": "ok", "message": "Server is running" }`

### Check Frontend Setup

1. Visit `http://localhost:3000`
2. Should see the application homepage

### Test User Registration

1. Go to Register page
2. Fill in the form
3. Click Register
4. You should receive a success message

## 🐛 Troubleshooting

Here are the issues I ran into while building this. Maybe it'll save you some time:

### Common Issues

#### Issue: MongoDB Connection Error
**What I did:**
- Check if MongoDB is actually running: `brew services list` (macOS)
- Verify the connection string in `.env` - one typo breaks everything
- If using Atlas, make sure your IP is whitelisted (or just use 0.0.0.0/0 for testing)

```bash
# Test MongoDB connection
mongosh "mongodb://localhost:27017/smart-community-helper"
```

#### Issue: Port Already in Use
This happens a lot. Kill whatever's using the port:

```bash
# Find what's using the port
lsof -i :5000  # For backend
lsof -i :3000  # For frontend

# Kill it
kill -9 <PID>
```

Or just restart your terminal. That's what I do when I'm lazy.

#### Issue: Module Not Found
Classic npm issue. Nuke it and start over:

```bash
# Delete everything
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

This fixes 90% of weird npm issues in my experience.

#### Issue: Google Maps Not Loading
**This drove me crazy:**
- Double-check your API key is correct (copied it wrong the first time)
- Make sure Maps JavaScript API is enabled in Google Cloud Console
- Check API restrictions - make sure localhost is allowed
- Billing MUST be enabled (Google requires it even on free tier)

If maps still don't work, check browser console for errors. Usually tells you what's wrong.

#### Issue: OpenAI API Errors
**Things to check:**
- API key is correct (no extra spaces)
- You have credits in your OpenAI account
- Rate limits not exceeded (check your usage dashboard)
- Make sure you're using the right model in your code

The API is expensive, so keep an eye on usage!

### Database Reset

```bash
# Connect to MongoDB
mongosh

# Drop database
use smart-community-helper
db.dropDatabase()

# Run seeder again
cd backend
npm run seed
```

## 🔐 Security Notes

Important stuff I learned the hard way:

1. **Never commit `.env` files** - Already in `.gitignore` but double-check!
2. **Use strong JWT secrets** - Generate with `openssl rand -base64 32` or just use a password generator
3. **Enable HTTPS in production** - Seriously, don't skip this
4. **Limit API rates** - Add rate limiting or you'll get hammered
5. **Validate all inputs** - Express-validator is your friend here
6. **Sanitize user data** - Had an XSS vulnerability in my first version. Oops.
7. **Use environment variables** - Never hardcode secrets, I've seen too many people do this

If you're deploying this, make sure you update all these secrets!

## 📚 Next Steps

If you got this far without breaking anything, congrats! 🎉

Here's what to do next:
1. Browse [FEATURES.md](FEATURES.md) to see what features exist
2. Check [TECH_STACK.md](TECH_STACK.md) to understand the tech choices
3. Actually read the code (I know, shocking)
4. Test the API endpoints (use Postman or curl)
5. Try adding a feature or fixing a bug

If you're new to React or Node.js, start with the frontend or backend folder separately. Don't try to understand everything at once!

## 🤝 Getting Help

- **Documentation**: Check the docs folder
- **Issues**: Report bugs on GitHub Issues
- **Discussions**: Ask questions in GitHub Discussions
- **Email**: Contact maintainers

## ✅ Setup Checklist

Did everything work? Check these off:

- [ ] Node.js installed and working
- [ ] MongoDB running (local or Atlas)
- [ ] Environment variables all filled in correctly
- [ ] All dependencies installed without errors
- [ ] Backend server starts without crashing
- [ ] Frontend server starts without crashing
- [ ] Can actually access the app at localhost:3000
- [ ] Can register a new user account
- [ ] Can log in with registered account
- [ ] Can create an issue (main feature!)
- [ ] Maps actually load on the page
- [ ] AI suggestions appear when reporting issues

If you checked all these, you're good to go! 🎉

---

Questions? Issues? Open a GitHub issue and I'll try to help!

Happy coding! 🚀

