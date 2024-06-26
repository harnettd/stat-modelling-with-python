from pandas import DataFrame
import requests


def get(url: str, params: dict, headers: dict) -> requests.Response | None:
    """
    Return the response from a get request (or None if the request fails).

    Use Response.raise_for_status() within a try-except-else block to print
    an error message rather than raise an exception.
    """
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
    except requests.HTTPError as err:
        print(f'get request failed, {err}')
        return None
    else:
        return response

def export(df: DataFrame, basename: str) -> None:
    """
    Export a DataFrame to a CSV file.
    """
    # the data directory
    dirname = '../data/'
    
    filename = dirname + basename
    df.to_csv(filename, index=False)


if __name__ == '__main__':
    pass
