"""
----------------------------------------------AMOUNT CONTROL------------------------------------------------------------
    Here you define the quantity or % of tokens for exchanges, adding liquidity, deposits, and transfers
    The software takes % only for ETH, other tokens are taken at 100% of the balance

    You can specify minimum/maximum amount or minimum/maximum % of the balance

    Quantity - (0.01, 0.02)
    Percentage - ("55", "60") ⚠️ Values in quotes

    AMOUNT_PERCENT_WRAPS
    AMOUNT_PERCENT | Specify only %, without quotes. Can be specified with precision up to 6 digits (99.123456, 99.654321).
                     ⚠️Other amount settings should be specified in quotes (if you want to work in %)⚠️
    MIN_BALANCE | Minimum balance for the account. With a lower balance, there will be an error: (Insufficient balance on account!)
"""
AMOUNT_PERCENT = (0.1, 0.2)  # Applied for exchanges.
AMOUNT_PERCENT_WRAPS = (55, 60)  # Applied for the wrap_abuser module.
LIQUIDITY_AMOUNT = (0.00001, 0.00002)  # Applied for adding liquidity, deposits to lendings, and wrap ETH
TRANSFER_AMOUNT = (0.0001, 0.0002)  # Applied for transfers of ether to your own or random address
MIN_BALANCE = 0.001  # Amount of ETH on the account

"""
------------------------------------------------GENERAL SETTINGS--------------------------------------------------------
    GLOBAL_NETWORK | Blockchain for main interaction ⚠️

    Arbitrum = 1            Scroll = 8
    Arbitrum Nova = 2       Starknet = 9
    Base = 3                Polygon ZKEVM = 10
    Linea = 4               zkSync Era = 11
    Manta = 5               Zora = 12
    Polygon = 6             Ethereum = 13
    Optimism = 7            Blast = 49

    WALLETS_TO_WORK = 0 | The software will take wallets from the table according to the rules described below
    0       = all wallets in sequence
    3       = only wallet #3
    4, 20   = wallet #4 and #20
    [5, 25] = wallets from #5 to #25
    
    ACCOUNTS_IN_STREAM      | Number of wallets in the stream for execution. If there are 100 wallets total, and you specify 10,
                             the software will make 10 approaches with 10 wallets each
    CONTROL_TIMES_FOR_SLEEP | Number of checks after which random sleep will be enabled for all accounts at
                             the moment when gas drops to MAXIMUM_GWEI and accounts will continue working

    EXCEL_PASSWORD          | Enables password request when entering the software. First set the password in the table
    EXCEL_PAGE_NAME         | Name of the sheet in the table. Example: 'EVM'
    GOOGLE_SHEET_URL        | Link to your Google spreadsheet with account progress
    GOOGLE_SHEET_PAGE_NAME  | Same as EXCEL_PAGE_NAME
    MAIN_PROXY              | Proxy for accessing exchange APIs. Format - log:pass@ip:port. Default - localhost
"""
GLOBAL_NETWORK = 3              # Any network from those specified above
SOFTWARE_MODE = 0               # 0 - sequential launch / 1 - parallel launch
ACCOUNTS_IN_STREAM = 1          # Only for SOFTWARE_MODE = 1 (parallel launch)
WALLETS_TO_WORK = 0             # 0 / 3 / 3, 20 / [3, 20]
SHUFFLE_WALLETS = False         # Shuffles wallets before launch
SHUFFLE_ROUTE = False           # Shuffles the route before launch
BREAK_ROUTE = False             # Stops route execution if an error occurs
VOLUME_MODE = False             # Pauses route execution when errors occur with exchanges or bridges
STOP_SOFTWARE = False           # Stops the entire software if a critical error occurs
SAVE_PROGRESS = True            # Enables saving account progress for Classic-routes
TELEGRAM_NOTIFICATIONS = False  # Enables Telegram notifications

'------------------------------------------------SLEEP CONTROL---------------------------------------------------------'
SLEEP_MODE = False               # Enables sleep after each module and account
SLEEP_TIME_MODULES = (60, 80)    # (minimum, maximum) seconds | Sleep time between modules.
SLEEP_TIME_ACCOUNTS = (40, 60)   # (minimum, maximum) seconds | Sleep time between accounts.

'-------------------------------------------------GAS CONTROL----------------------------------------------------------'
GAS_CONTROL = False             # Enables gas control
MAXIMUM_GWEI = 40               # Maximum GWEI for software operation, change during software operation in maximum_gwei.json
SLEEP_TIME_GAS = 100            # Time for the next gas check
CONTROL_TIMES_FOR_SLEEP = 5     # Number of checks
GAS_LIMIT_MULTIPLIER = 1.5      # Gas limit multiplier for transactions. Helps save on transactions
GAS_PRICE_MULTIPLIER = 1.3      # Gas price multiplier for transactions. Speeds up execution or reduces transaction price

'------------------------------------------------RETRY CONTROL---------------------------------------------------------'
MAXIMUM_RETRY = 20              # Number of retries on errors
SLEEP_TIME_RETRY = (5, 10)      # (minimum, maximum) seconds | Sleep time after another retry

'------------------------------------------------PROXY CONTROL---------------------------------------------------------'
USE_PROXY = False                # Enables proxy usage
MOBILE_PROXY = False             # Enables mobile proxy usage. USE_PROXY must be True
MOBILE_PROXY_URL_CHANGER = [
    '',
]  # ['link1', 'link2'..] | Links for changing IP. The software will go through all links

'-----------------------------------------------SLIPPAGE CONTROL-------------------------------------------------------'
SLIPPAGE = 2                   # 0.54321 = 0.54321%, 1 = 1% | Maximum price impact when exchanging tokens

'-----------------------------------------------APPROVE CONTROL--------------------------------------------------------'
UNLIMITED_APPROVE = False       # Enables unlimited Approve for the contract

'------------------------------------------------HELP SOFTWARE---------------------------------------------------------'
HELP_SOFTWARE = False  # Enables transferring 1% of the swap amount to the author when working with aggregators. Transfer goes from the contract.

'------------------------------------------------PROXY CONTROL---------------------------------------------------------'
MAIN_PROXY = ''                  # log:pass@ip:port, proxy for accessing exchange APIs. Default - localhost

'------------------------------------------------SECURE DATA-----------------------------------------------------------'
# OKX API KEYS https://www.okx.com/ru/account/my-api
OKX_API_KEY = ""
OKX_API_SECRET = ""
OKX_API_PASSPHRAS = ""
OKX_EU_TYPE = False

# BITGET API KEYS https://www.bitget.com/ru/account/newapi
BITGET_API_KEY = ""
BITGET_API_SECRET = ""
BITGET_API_PASSPHRAS = ""

# BINGX API KEYS https://bingx.com/ru-ru/account/api/
BINGX_API_KEY = ""
BINGX_API_SECRET = ""

# BINANCE API KEYS https://www.binance.com/ru/my/settings/api-management
BINANCE_API_KEY = ""
BINANCE_API_SECRET = ""

# EXCEL AND GOOGLE INFO
EXCEL_PASSWORD = False
EXCEL_PAGE_NAME = "EVM"
EXCEL_FILE_PATH = "./data/accounts_data.xlsx"  # You can leave unchanged if the default table location is suitable
GOOGLE_SHEET_URL = ""
GOOGLE_SHEET_PAGE_NAME = ""

# TELEGRAM DATA
TG_TOKEN = ""  # https://t.me/BotFather
TG_ID = ""  # https://t.me/getmyid_bot

# INCH API KEY https://portal.1inch.dev/dashboard
ONEINCH_API_KEY = ""

# LAYERSWAP API KEY https://www.layerswap.io/dashboard
LAYERSWAP_API_KEY = ""
