# 💻 Code Snippets

This folder contains important code examples and snippets from the Smart Community Helper project.

## 📁 Folder Structure

```
code-snippets/
├── README.md (this file)
├── backend/
│   ├── auth-controller.js (Authentication logic)
│   ├── issue-controller.js (Issue management)
│   ├── ai-service.js (AI integration)
│   └── socket-events.js (Real-time events)
├── frontend/
│   ├── components/
│   │   ├── IssueForm.jsx (Issue reporting form)
│   │   ├── MapView.jsx (Google Maps integration)
│   │   └── Dashboard.jsx (Dashboard component)
│   └── hooks/
│       ├── useAuth.js (Authentication hook)
│       └── useIssues.js (Issues data hook)
└── ai/
    ├── category-classifier.js (AI categorization)
    └── solution-generator.js (Solution generation)
```

## 📝 Code Snippet Guidelines

### Formatting
- Use consistent indentation (2 spaces please)
- Add comments for complex logic
- Include function descriptions
- Show import statements at the top

### Best Practices
- Focus on key functionality
- Include error handling
- Show both frontend and backend examples
- Demonstrate AI integration patterns
- Highlight security measures

## 🎯 Important Code Areas

### Backend
- **Authentication**: JWT implementation, password hashing
- **API Routes**: RESTful endpoint examples
- **Database**: Mongoose models and queries
- **AI Integration**: OpenAI API usage
- **Real-time**: Socket.io implementation

### Frontend
- **Components**: Reusable React components
- **State Management**: Redux slices and actions
- **API Calls**: Axios interceptors and requests
- **Maps**: Google Maps API integration
- **Forms**: Form validation and submission

### AI Integration
- **Categorization**: NLP-based issue classification
- **Solution Generation**: AI-powered recommendations
- **Chatbot**: Conversational AI implementation

## 📚 Code Examples

### Authentication Example
```javascript
// Example: JWT token generation
const token = jwt.sign(
  { userId: user._id },
  process.env.JWT_SECRET,
  { expiresIn: '7d' }
);
```

### API Call Example
```javascript
// Example: Creating an issue
const createIssue = async (issueData) => {
  const response = await axios.post('/api/issues', issueData);
  return response.data;
};
```

### AI Integration Example
```javascript
// Example: Generating AI suggestions
const generateSuggestions = async (issueDescription) => {
  const response = await openai.chat.completions.create({
    model: 'gpt-4',
    messages: [{ role: 'user', content: issueDescription }]
  });
  return response.choices[0].message.content;
};
```

## 🔒 Security Notes

- Never commit API keys or secrets
- Use environment variables for sensitive data
- Implement proper validation and sanitization
- Use HTTPS in production
- Implement rate limiting

## 🚀 Quick Reference

### Most Important Files
1. Backend authentication controller
2. Frontend issue form component
3. AI service integration
4. Socket.io event handlers
5. Google Maps integration

### Key Patterns
- RESTful API design
- Component-based architecture
- Redux state management
- AI prompt engineering
- Real-time updates

---

**Note**: Add your code snippets here to help others learn from your implementation! Make sure the code actually works though - I've seen too many snippets with bugs.

