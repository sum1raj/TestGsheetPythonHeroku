import gspread

cred_json = {
  "type": "service_account",
  "project_id": "gsheetpythonheroku",
  "private_key_id": "e476b33e8a1ddf6a2bc910d37412b1cfb3ac4023",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCquIsYwLaVlQ6w\ns9o3rBVcQMw0i33rTTKnBADkhsqmhCxzA9oIIYnQBLpTYFzgNLuhNR8FTFufANzh\nhjGGGKPFVr0rjE/0G96st6uzXzEtLiBPpJM6er3aaUAwSWqHZvmsvV9JQI0d3/BZ\nWYimUCxd00zmVvbq4UMLebI7vcJGWQvzvY8VkUjtgRCYnQX8qlAE664EjtdVdW4E\nvHSOdLCPdVh08hRsrxm0oTsOTwcHJ+TAhu80qfI6mc3BvlCxPSSyqXJs4fVWKEFn\nicB8QkTdwgSs8TNFAQ1GZ58edH4SkSPnCjvCBveJRTcu+W5FgqRAHfVhgRDv2m4Y\nCc7TNr8JAgMBAAECggEABrkNtGo7+aTNCn6915A0DYksgXhplQKNPbAV31BcWpvw\nRCpt3TQbTgQucjbkcWlvAIIr0cGYBtyGowe6m4hzRCon31C/NUjqE+y659PJbZLY\nPH3dB/u3AXFAaqZf4F6/WXx7n1INCWG9AHr0iD6DM/UTA8V/VvCLLo1N5ekrGJBv\nDa2CkZu2/lo7zShzApqo8corXMuqgPTWM3oy29kIljSBgaJWRAcFPxRqzMrlhnuM\n94ryTjLVDXTUghUwr/Tm6BCERV3kt+yHjnX16XB+29P4LR+zyGon5B8toGeoCoam\n/PSpB0rGgKiSxy1WAn8ubJkzqcZ0EPODJSCv36FtIQKBgQDbXSQLWhJHIZLN9cD7\nKnZpdcbtVYMmNXH2lrcnS/YcAvxS0F7INn2+wHruHrogYTcgCWZQj3GfxTgdqni9\nrS+rhSWEJbGVY56Eam756LI0BBoQLYyCe4viogMLwt1PG8CmnLcfXkuc2KJgYEUd\nuFkrbb+k1fL2DkVZop9gRliyswKBgQDHO66ZPuuBWn1cuZwQtTsqrkJlhyWhlstd\n2KJudx4e3G8NSWlodzdCisJxov6H64H2uD856MwTlJ6YtaezMxyBQWlQQPF6MUN7\nJQdL8+Y3Ti+7QN+Z68jvdI37/UTEuqJQLRPToCQBJ3F06Gd13W5CzXxI8vurryd7\nFLLIqpN1UwKBgQCI4tZbPxmoyYqSe4ixMw4xQQ2hjHsKnM9A0Uv5ea1aTYKnKt/6\nkAZnwjTz4rjC++cqVrNCEkEVMjySRo6RzkCxB6UhkWP/lOqWNtSJnmuVifm5nrLP\nucjQ48iCzlbLxsWxMpoTOQR2G7k36ts2cJM0RogQlHHImZ8tEA3kRgGTgQKBgQCi\nqvsKilH04nI6tB1VkvNFDNSPWsIB5kITVJ6CvOUt42MUoRzcO4I15V+PMrrJNSN+\n0r5kxMtjLVQ0cRUEfjXG3yZibTP8RZ7IO9pyTChqfX8BT52Baf88a5jF5uswCQYf\nmj526mibPJ4pCtv2Yx30kxvn3+RWMAN3PdYfew48mwKBgA8YOY9wpmybz/EKdvFN\ngViBWRKNlyJA437lRqs/d0EAptEZwUFxkhphbC+BA6a4IfkHJEM6EOtTXDUgNTCG\nfU6Ogvg1GQLJXxVMTHXHITC+6YBHB/CoNh9Lf8AK0NJkiHeA34sUm4pJTX/CPrPL\nBgoHmrNplcaMUJ/RX+YQUAnc\n-----END PRIVATE KEY-----\n",
  "client_email": "gsheet-python-heroku@gsheetpythonheroku.iam.gserviceaccount.com",
  "client_id": "116100010438919647812",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/gsheet-python-heroku%40gsheetpythonheroku.iam.gserviceaccount.com"
}
sa = gspread.service_account_from_dict(cred_json)
sh = sa.open('GSheetPYthonHEroku')
ws = sh.worksheet('Sheet1')
ws.update('A1', 'Avanshika')