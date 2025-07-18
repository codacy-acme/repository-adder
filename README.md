# Codacy Integration Helper

A Python tool for bulk adding repositories to Codacy and configuring their integration settings. This utility helps automate the process of onboarding multiple repositories to Codacy's code quality platform.

## Features

- 📦 **Bulk Repository Addition**: Add multiple repositories to Codacy from a simple text file
- 🔧 **Integration Settings Configuration**: Automatically configure repository integration settings
- 🌐 **Multiple Provider Support**: Works with GitHub (gh) and GitHub Enterprise (ghe)
- ⚡ **Rate Limiting**: Built-in delays to respect API rate limits
- 🛡️ **Error Handling**: Comprehensive error handling with detailed feedback
- 🏢 **Organization Support**: Add repositories under specific organizations

## Requirements

- Python 3.6+
- `requests` library (see requirements.txt)
- Codacy API token with appropriate permissions

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd repository-adder
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python main.py --token YOUR_API_TOKEN --file repositories.txt --provider gh --organization your-org
```

### Parameters

| Parameter | Required | Description | Default |
|-----------|----------|-------------|---------|
| `--token` | ✅ | Codacy API token | - |
| `--file` | ✅ | Path to text file containing repository names | - |
| `--provider` | ✅ | Git provider (`gh` for GitHub, `ghe` for GitHub Enterprise) | - |
| `--organization` | ✅ | Organization name | - |
| `--baseurl` | ❌ | Codacy server address | `https://app.codacy.com` |

### Repository File Format

Create a text file with one repository name per line:

```
repository-name-1
repository-name-2
my-awesome-project
another-repo
```

### Example Commands

**Adding repositories to Codacy Cloud:**
```bash
python main.py --token abc123def456 --file repos.txt --provider gh --organization organization
```

**Adding repositories to Codacy Self-hosted:**
```bash
python main.py --token abc123def456 --file repos.txt --provider ghe --organization my-org --baseurl https://codacy.mycompany.com
```

## Integration Settings

The tool automatically configures the following integration settings for each repository:

- ❌ Commit Status: Disabled
- ❌ Pull Request Comments: Disabled
- ❌ Pull Request Summary: Disabled
- ❌ Coverage Summary: Disabled
- ❌ Suggestions: Disabled
- ❌ AI Enhanced Comments: Disabled

To modify these settings, edit the `data` object in the `update_repository_integrations_settings` function.

## Error Handling

The tool handles various scenarios gracefully:

- **409 Conflict**: Repository already exists (non-fatal)
- **API Errors**: Network issues, authentication failures, etc.
- **Rate Limiting**: 2-second delay between requests

## API Endpoints Used

- `POST /api/v3/repositories` - Add repository
- `PATCH /api/v3/organizations/{provider}/{organization}/repositories/{repository}/integrations/providerSettings` - Update integration settings

## Getting Your API Token

1. Log in to your Codacy instance
2. Go to Account Settings → API Tokens
3. Generate a new token with repository management permissions
4. Copy the token for use with this tool

## Troubleshooting

### Common Issues

**Authentication Error (401)**
- Verify your API token is correct and has sufficient permissions

**Repository Already Exists (409)**
- This is expected behavior when a repository is already added to Codacy
- The tool will skip these repositories and continue processing

**Rate Limiting (429)**
- The tool includes automatic delays, but you may need to adjust the sleep time in `process_files()`

### Debug Mode

For detailed debugging, you can modify the script to print response details:

```python
print(f"Response Status: {response.status_code}")
print(f"Response Body: {response.text}")
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

[Add your license information here]

## Support

For issues and questions:
- Check the [troubleshooting section](#troubleshooting)
- Review Codacy's API documentation
- Open an issue in this repository

---

**Note**: This tool is designed for bulk operations. For single repository additions, consider using the Codacy web interface.