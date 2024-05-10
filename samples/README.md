# Krutrim AI Cloud Inference Service Samples

This repository consists of sample code to interact with the Krutrim Chat Completion APIs.

## Prerequisites

Before you begin, ensure that you have the following:
- Python 3.10+ installed on your system
- Krutrim API key

## Installation

### 1. **Clone the Repository** 

```bash
git clone https://github.com/ola-krutrim/ai-cloud.git
```

### 2. **Install Dependencies**

Create a virtual environment and activate it:

```bash
cd samples
python3 -m venv venv
source venv/bin/activate
```

Install the required Python packages:

```bash
pip3 install -r requirements.txt
```

## Configuration
To configure your application, you'll need to set up your Krutrim API key. 

You can do this by setting the `API_KEY` environment variable

-  In the [sample.env](./sample.env) and rename the file to `.env`:

**OR**

- Using `export`:

```bash
export API_KEY='your-api-key'
```
