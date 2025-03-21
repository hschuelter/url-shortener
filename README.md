# encurta.ai - an url shortener

## 📚 Overview

This repository contains the implementation of an url shortener prototype. It is currently available at https://encurta-ai.vercel.app/ 

The primary focus of this repository is to practice the develop the full life cycle of a project, from planning, to development and, finally, to deployment. Also, it's an excuse to practice this tech stack.

## 🛠️ Tech Stack

- **Backend**: FastAPI.
- **Frontend**: Tailwind CSS + Shadcn.
- **Deployment**: Vercel and Koyeb.

## 📂 Repository Structure

```
├── api/                                # Backend implementation.
│   ├── Data/                           # Classes for the JSON format received in the backend.
│   ├── Repository/                     # Classes that interact with the database.
│   ├── Services/                       # Classes that implement the requests behavior. 
│   └── server.py                       # API configuration and requests handling.
├── ui/                                 # Frontend implementation.
└── README.md                           # Project documentation.
```

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hschuelter/url-shortener.git
   cd url-shortener
   ```

2. **Setting up the environment**:
   - **Set up the backend**:
   
   Install the requirements:
    ```bash
    cd api/
    python -m venv .venv
    source .venv/bin/activate
    pip install requirements.txt
   ```

   - **Set up the frontend**:
   
    Install the requirements:
    ```bash
    cd ui/
    npm install
    ```

3. **Running locally**:
   - For the backend:
     ```bash
     fastapi dev server.py 
     ```
   - For the backend:
     ```bash
     npm run dev
     ```

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests to help improve the repository.

1. Fork the repository.
2. Create your feature branch:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a pull request.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.