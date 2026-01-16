import pyodbc
def get_connection():
    conn_str = (
        "Driver={ODBC Driver 18 for SQL Server};"
        "Server=tcp:2cogp2dcasiulp6fuvn3gpkvma-rjajwny5yjzu3hozc2i6pstuhi.datawarehouse.fabric.microsoft.com,1433;"
        "Database=lakers;"
        "Authentication=ActiveDirectoryInteractive;"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
    )
    return pyodbc.connect(conn_str)
