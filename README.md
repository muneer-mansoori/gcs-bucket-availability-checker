# Google Cloud Storage Bucket Name Availability Checker

A simple Python utility to check whether Google Cloud Storage bucket names are available for creation. This tool is particularly useful for developers and DevOps engineers who need to verify bucket name availability before attempting to create new buckets programmatically.

## Features

- ✅ Check multiple bucket names at once
- ✅ Clear status reporting (available/not available/unknown)
- ✅ Proper error handling for different scenarios
- ✅ Logging support for debugging
- ✅ Type hints for better code maintainability
- ✅ Easy to integrate into existing projects

## Prerequisites

- Python 3.7 or higher
- Google Cloud SDK installed and configured
- Valid Google Cloud credentials

## Installation

1. Clone this repository or download the script
2. Install the required dependencies:

```bash
pip install google-cloud-storage
```

3. Ensure you have Google Cloud credentials configured:
   - Via `gcloud auth application-default login`, or
   - By setting the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to your service account key file

## Usage

### Basic Usage

```python
from check_bucket_name_availability import check_bucket_availability

bucket_names = [
    "my-unique-bucket-name",
    "another-bucket-name",
    "test-bucket-2024"
]

check_bucket_availability(bucket_names)
```

### Command Line Usage

```bash
python check-bucket-name-availability.py
```

### Sample Output

```
Google Cloud Storage Bucket Name Availability Checker
=======================================================
Checking 5 bucket names...

"example-bucket-1" = not available
"example-bucket-2" = available
"example-bucket-3" = available
"my-unique-project-bucket-2024" = available
"test-bucket-availability-check" = unknown (permission denied)

Check completed!
```

## Status Meanings

- **available**: The bucket name is available and can be used
- **not available**: The bucket name is already taken
- **unknown (permission denied)**: The bucket exists but you don't have permission to access it
- **check failed**: An error occurred while checking the bucket

## Configuration

You can modify the `bucket_list` in the `main()` function to check your own bucket names:

```python
bucket_list = [
    "your-bucket-name-1",
    "your-bucket-name-2",
    # Add more names here
]
```

## Error Handling

The script handles various scenarios:
- Network connectivity issues
- Authentication problems
- API rate limiting
- Invalid bucket names
- Permission errors

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is provided as-is for educational and utility purposes. Always verify bucket availability through official Google Cloud documentation and tools for production use.

## Author

Created for the developer community to simplify GCS bucket name validation.
