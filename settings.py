"""
----------------------------------------------------CEX CONTROL---------------------------------------------------------
    Select networks/amounts for withdrawal and deposit from CEX. Don't forget to insert API keys in general_settings.py.
    Deposits and withdrawals work only with spot balance on the exchange.

    1 - ETH-ERC20                11 - GLMR-Moonbeam       21 - USDT-Optimism             31 - USDC-BSC
    2 - ETH-Arbitrum One         12 - MOVR-Moonriver      22 - USDT-Polygon              32 - USDC-ERC20
    3 - ETH-Optimism             13 - METIS-Metis         23 - USDT-BSC                  33 - STG-Arbitrum One
    4 - ETH-zkSync Era           14 - CORE-CORE           24 - USDT-ERC20                34 - STG-BSC
    5 - ETH-Linea                15 - CFX-CFX_EVM         25 - USDC-Arbitrum One         35 - STG-Avalanche C-Chain
    6 - ETH-Base                 16 - KLAY-Klaytn         26 - USDC-Avalanche C-Chain    36 - STG-Fantom
    7 - AVAX-Avalanche C-Chain   17 - FTM-Fantom          27 - USDC-Optimism             37 - USDV-BSC
    8 - BNB-BSC                  18 - POL-Polygon       28 - USDC-Polygon              38 - ARB-Arbitrum One
    9 - BNB-OPBNB                19 - USDT-Arbitrum One   29 - USDC-Optimism (Bridged)   39 - MAV-Base
    10 - CELO-CELO               20 - USDT-Avalanche      30 - USDC-Polygon (Bridged)    40 - MAV-zkSync Era
                                                                                         41 - OP-Optimism

    ⚠️ The software automatically subtracts the commission from the deposit amount when working with native tokens ⚠️

    Amount in quantity  - (0.01, 0.02)
    Amount in percentage  - ("10", "20") ⚠️ Values in quotes.

    OKX_WITHDRAW_DATA | Each list is one module for withdrawal from the exchange. Examples are shown below:
                        For each withdrawal, specify [withdrawal network, (min and max amount)]

    OKX_DEPOSIT_DATA | Each list is one module for deposit to the exchange. Examples are shown below:
                       For each deposit, specify [deposit network, (min and max amount), limiterX, limiterY]

                       Settings for limited deposit to the exchange. Specify in $USD
                       limiterX - minimum balance on the account for the software to start the withdrawal process
                       limiterY - min. and max. amount that should remain on the balance after withdrawal.
                       If the deposit amount will leave the account balance greater than the 2nd value, the software will not
                       try to make the deposit amount larger or smaller than specified in DEPOSIT_DATA


    Examples of randomizing withdrawal from the exchange:

    [[17, (1, 1.011)], None] | Example of setting None for random choice (performing the action or skipping it)
    [[2, (0.48, 0.5)], [3, (0.48, 0.5)]] | Example of setting two networks, the software will choose one random network.

    In addition to the above examples, the balance search mode is supported for deposits to the exchange:
        [(2, 3, 4), (0.001, 0.002), 0, (0, 0)] | Example of specifying multiple networks, the software will choose the network
                                                 with the largest balance.

    CEX_BALANCER_CONFIG = [
        [X, Y, Z],
    ]

    "X" - The software will check the amount of this token in this network, according to the list in the "CEX CONTROL" group
    If the token amount is less than value "Y", then withdrawal occurs from exchange "Z" of token "X" in an amount equal to the difference
    between the balance and the desired amount of tokens on the balance.
    "Z" value - exchange for withdrawal. 1 - OKX, 2 - BingX, 3 - Binance, 4 - Bitget. You can specify several in parentheses,
    the software will choose one exchange. Module (make_balance_to_average).

    Example:
    CEX_BALANCER_CONFIG = [
        [20, 5, 1],
    ]

    The software checks USDT in the Avalanche network. If less than 5, and the balance is 2.1, the software adds 2.9 USDT from the exchange
"""

WAIT_FOR_RECEIPT_CEX = True  # If True, will wait for receipt of funds in the incoming network after deposit/withdrawal
COLLECT_FROM_SUB_CEX = True  # If True, will collect funds before/after deposit/withdrawal from subs to main account

'--------------------------------------------------------OKX-----------------------------------------------------------'

OKX_WITHDRAW_DATA = [
    [6, (0.00011, 0.00012)],
]

OKX_DEPOSIT_DATA = [
    [1, ('100', '100'), 0, (0, 0)],
]

'--------------------------------------------------------BingX---------------------------------------------------------'

BINGX_WITHDRAW_DATA = [
    [8, (0.004, 0.00411)],
]

BINGX_DEPOSIT_DATA = [
    [37, ('100', '100'), 0, (0, 0)],
]

'-------------------------------------------------------Binance--------------------------------------------------------'

BINANCE_WITHDRAW_DATA = [
    [8, (0.004, 0.00411)],
]

BINANCE_DEPOSIT_DATA = [
    [37, ('100', '100'), 0, (0, 0)],
]

'--------------------------------------------------------BitGet--------------------------------------------------------'

BITGET_WITHDRAW_DATA = [
    [33, ('100', '100')],
]

BITGET_DEPOSIT_DATA = [
    [33, ('100', '100'), 0, (0, 0)],
]

'-------------------------------------------------------Control--------------------------------------------------------'

CEX_BALANCER_CONFIG = [
    [1, 0.005, 3]
]

"""
-----------------------------------------------------BRIDGE CONTROL-----------------------------------------------------
    Check manually if the network works on the website. (The software will check itself, but why stress it?)
    Don't forget to insert the API key for LayerSwap below. Each bridge supports unique configuration
       
        Arbitrum = 1                    zkSync Era = 11        Mode = 50
        Arbitrum Nova = 2               Zora = 12 
        Base = 3                        Ethereum = 13
        Linea = 4                       Avalanche = 14
        Manta = 5                       BNB Chain = 15
        Polygon = 6                     Metis = 26        
        Optimism = 7                    OpBNB = 28
        Scroll = 8                      Mantle = 29
        Starknet = 9                    ZKFair = 45
        Polygon zkEVM = 10              Blast = 49
                                           
    Amount in quantity  - (0.01, 0.02)
    Amount in percentage  - ("10", "20") ⚠️ Values in quotes
    
    NATIVE_CHAIN_ID_FROM(TO) = [2, 4, 16] | One of the networks will be chosen. Applicable for bridge_zora (instant), 
                                            other bridges in L2 will be from Ethereum, and withdrawals to Ethereum
    NATIVE_DEPOSIT_AMOUNT | Setting for withdrawal from native bridge (withdraw_native_bridge)
    ACROSS_TOKEN_NAME | Specify the token for the bridge. Supported: ETH, BNB, MATIC, USDC, USDC.e (Bridged), USDT. 
                        If the bridge has 2 tokens in parentheses, see BUNGEE_TOKEN_NAME, the bridge can make bridges
                        between different tokens. To the right of the parameter, available tokens are listed for each bridge.
                        
    ACROSS_AMOUNT_LIMITER | Setting for limited bridges. Specify in $USD
                            1st value - minimum balance on the account for the software to start the bridge process
                            2nd value - min. and max. amount that should remain on the balance after bridge
                            If the bridge amount will leave the account balance greater than the second value,
                            the software will not try to make the bridge amount larger or smaller than specified
                    
    BUNGEE_ROUTE_TYPE | Setting your own route for transaction, by default (0) - the best one. 
                        1-Across   3-Celer     5-Stargate   7-Synapse      9-Hop
                        2-CCTP     4-Connext   6-Socket     8-Symbiosis    10-Hyphen   
    
    BRIDGE_SWITCH_CONTROL | Allows using the same bridge twice. By default, each number is assigned to
                            its own bridge (see values below), to change this setting
                            follow the dependencies below and specify a unique setting value for each bridge,
                            by which it will work.
                            
                            1-ACROSS     3-LAYERSWAP    5-ORBITER     7-RELAY
                            2-BUNGEE     4-NITRO        6-OWLTO       8-RHINO
                                            
"""

WAIT_FOR_RECEIPT_BRIDGE = True  # If True, will wait for receipt of funds in the incoming network after bridge

'-----------------------------------------------------Native Bridge----------------------------------------------------'

NATIVE_CHAIN_ID_FROM = [3]                 # Outgoing network. Applicable only for bridge_zora, others from Ethereum
NATIVE_CHAIN_ID_TO = [13]                  # Incoming network. Applicable only for bridge_zora, others to Ethereum
NATIVE_BRIDGE_AMOUNT = (0.001, 0.001)      # (minimum, maximum) (% or quantity)
NATIVE_TOKEN_NAME = 'ETH'
NATIVE_AMOUNT_LIMITER = 0, (0, 0)

'--------------------------------------------------------Across--------------------------------------------------------'

ACROSS_CHAIN_ID_FROM = [6]                # Outgoing network
ACROSS_CHAIN_ID_TO = [11]                 # Incoming network
ACROSS_BRIDGE_AMOUNT = (1, 1)             # (minimum, maximum) (% or quantity)
ACROSS_TOKEN_NAME = 'USDT'
ACROSS_AMOUNT_LIMITER = 0, (0, 0)

'--------------------------------------------------------Bungee--------------------------------------------------------'

BUNGEE_CHAIN_ID_FROM = [10]                  # Outgoing network
BUNGEE_CHAIN_ID_TO = [11]                    # Incoming network
BUNGEE_BRIDGE_AMOUNT = (0.001, 0.003)       # (minimum, maximum) (% or quantity)
BUNGEE_TOKEN_NAME = ('ETH', 'ETH')          # ETH, BNB, MATIC, USDC, USDC.e, USDT
BUNGEE_ROUTE_TYPE = 0                       # see BUNGEE_ROUTE_TYPE
BUNGEE_AMOUNT_LIMITER = 0, (0, 0)

'-------------------------------------------------------LayerSwap------------------------------------------------------'

LAYERSWAP_CHAIN_ID_FROM = [3]               # Outgoing network
LAYERSWAP_CHAIN_ID_TO = [1]                  # Incoming network
LAYERSWAP_BRIDGE_AMOUNT = (0.0012, 0.0012)     # (minimum, maximum) (% or quantity)
LAYERSWAP_TOKEN_NAME = ('ETH', 'ETH')     # ETH, USDC, USDC.e
LAYERSWAP_AMOUNT_LIMITER = 0, (0, 0)

'--------------------------------------------------------Nitro---------------------------------------------------------'

NITRO_CHAIN_ID_FROM = [1]                   # Outgoing network
NITRO_CHAIN_ID_TO = [11]                    # Incoming network
NITRO_BRIDGE_AMOUNT = (0.001, 0.001)        # (minimum, maximum) (% or quantity)
NITRO_TOKEN_NAME = ('ETH', 'USDC')          # ETH, USDC, USDT
NITRO_AMOUNT_LIMITER = 0, (0, 0)

'-------------------------------------------------------Orbiter--------------------------------------------------------'

ORBITER_CHAIN_ID_FROM = [7, 3, 5]           # Outgoing network
ORBITER_CHAIN_ID_TO = [6]                   # Incoming network
ORBITER_BRIDGE_AMOUNT = (8, 9)              # (minimum, maximum) (% or quantity)
ORBITER_TOKEN_NAME = 'USDC'
ORBITER_AMOUNT_LIMITER = 0, (0, 0)

'--------------------------------------------------------Owlto---------------------------------------------------------'

OWLTO_CHAIN_ID_FROM = [1]                 # Outgoing network
OWLTO_CHAIN_ID_TO = [11]                    # Incoming network
OWLTO_BRIDGE_AMOUNT = (0.001, 0.001)       # (minimum, maximum) (% or quantity)
OWLTO_TOKEN_NAME = 'ETH'
OWLTO_AMOUNT_LIMITER = 0, (0, 0)

'--------------------------------------------------------Relay---------------------------------------------------------'

RELAY_CHAIN_ID_FROM = [1]                # Outgoing network
RELAY_CHAIN_ID_TO = [50]                   # Incoming network
RELAY_BRIDGE_AMOUNT = (0.001, 0.001)      # (minimum, maximum) (% or quantity)
RELAY_TOKEN_NAME = 'ETH'
RELAY_AMOUNT_LIMITER = 0, (0, 0)

'--------------------------------------------------------Rhino---------------------------------------------------------'

RHINO_CHAIN_ID_FROM = [1]                # Outgoing network
RHINO_CHAIN_ID_TO = [13]                 # Incoming network
RHINO_BRIDGE_AMOUNT = (0.003, 0.003)           # (minimum, maximum) (% or quantity)
RHINO_TOKEN_NAME = ('ETH', 'ETH')       # ETH, BNB, MATIC, USDC, USDT
RHINO_AMOUNT_LIMITER = 0, (0, 0)

BRIDGE_SWITCH_CONTROL = {
    1: 1,  # ACROSS
    2: 2,  # BUNGEE
    3: 3,  # LAYERSWAP
    4: 4,  # NITRO
    5: 5,  # ORBITER
    6: 6,  # OWLTO
    7: 7,  # RELAY
    8: 8,  # RHINO
}

"""
---------------------------------------------OMNI-CHAIN CONTROL---------------------------------------------------------
    Check manually if the networks work on the website. (The software will check itself, but why stress it?)
       
        Arbitrum = 1                  Goerli = 16                        Optimism = 31
        Arbitrum Nova = 2             Gnosis = 17                        Orderly = 32
        Astar = 3                     Harmony = 18                       Polygon = 33  
        Aurora = 4                    Horizen = 19                       Polygon zkEVM = 34
        Avalanche = 5                 Kava = 20                          Scroll = 35
        BNB = 6                       Klaytn = 21                        ShimmerEVM = 36
        Base = 7                      Linea = 22                         Telos = 37
        Canto = 8                     Loot = 23                          TomoChain = 38 
        Celo = 9                      Manta = 24                         Tenet = 39
        Conflux = 10                  Mantle = 25                        XPLA = 40
        CoreDAO = 11                  Meter = 26                         Zora = 41  
        DFK = 12                      Metis = 27                         opBNB = 42
        Ethereum = 13                 Moonbeam = 28                      zkSync = 43
        Fantom = 14                   Moonriver = 29                     Beam = 44
        Fuse = 15                     OKX = 30                           inEVM = 45
                                                                         Rarible = 46
    
    All settings are shown in examples, similar settings by name work similarly
    
    STG_STAKE_CONFIG | [(Minimum, maximum months for lock), (minimum, maximum amount for lock)].
                        The software will stake STG in the network with the largest STG balance from STARGATE_CHAINS.
    
    STARGATE_AMOUNT | Determines what amount to send through the bridge. Supports % and quantity specification
    STARGATE_CHAINS | Choose chains between which bridges will be made
    STARGATE_TOKENS | Choose coins between which swaps will be made. 
                      Available: ETH, USDT, USDC, USDV, STG, MAV
    STARGATE_DUST_CONFIG |  Example: (['USDV', 'USDV'], [31, 6]). The software will send 0.000000(1-3)% of the token balance in the network with
                            the largest balance. Only applies to the bridge_stargate_dust module
    
        The software will determine where the balance is now and make a bridge according to the logic specified in the above settings    
        
        Specify tokens in the same order as chains. Conditionally STARGATE_CHAINS = [5, 6] and
        STARGATE_TOKENS = ['USDC', 'USDT'] will mean that for chain #5 it will be USDC, and for #6 USDT
        Swaps for ETH are made on the value from AMOUNT_PERCENT. 
        
        For Stargate, you can specify any number of networks, the software will make bridges to a random network from the list. 
        
        Stargate operation options:
        
        1) Circular bridge with entry from network. Specifying STARGATE_CHAINS = [1, (7, 22)], the software will make a bridge 
        from network '1' to the left one from the inner list '7', then there will be bridges between networks from the inner list, to 
        activate this mode you need to run the module once and specify the desired number of bridges L0_BRIDGE_COUNT.
        The last bridge will be to network '1'. You can specify more than two networks inside parentheses, the first bridge will also be to
        the leftmost one. You can specify several initial networks, example: STARGATE_CHAINS = [1, 2, (7, 22)],
        then the software will start and finish in a random network.
        
        2) Mode of touching each network. Specifying STARGATE_CHAINS = [1, 7, 22] and L0_BRIDGE_COUNT equal to the number of
        specified networks in STARGATE_CHAINS and running the module 1 time, the software will try to make a bridge from each specified
        network. When specifying L0_BRIDGE_COUNT > STARGATE_CHAINS, after attempts to bridge from each network, the software will choose
        a random network
        
        3) Strict route mode. Specifying STARGATE_CHAINS = (1, 7, 22) and running the module 1 time, the software will make
        bridges in sequence from each specified network (i) to the next (i + 1). L0_BRIDGE_COUNT must be strictly equal to
        the length of STARGATE_CHAINS - 1 
        
        4) Random networks mode. Specifying STARGATE_CHAINS = [1, 7, 22] and L0_BRIDGE_COUNT equal to 1, running the module 1 time,
        the software will find where the balance is now and make 1 bridge to another random network from the list.
        
        For CoreDAO, 3-leg and 2-leg bridges are available, as well as strict route mode.
        Bridge from the first network in order in COREDAO_CHAINS, then to CoreDAO, then to the third network from COREDAO_CHAINS,
        if L0_BRIDGE_COUNT > 3, the software will make this order of bridges in a circle (1 - 2 - 3, and then 3 - 2 - 1)
        2-leg bridges work like a normal circular run (1 - 2, 2 - 1).
        
    L0_BRIDGE_COUNT | Number of bridges for one launch of bridge_stargate or bridge_coredao. If specified as a list,
                      the software will choose a random number. Example: L0_BRIDGE_COUNT = [4, 6, 8], one of
                      these values will be chosen, not a random one in between, but exactly one of these values.
                      
    L0_SEARCH_DATA | Setting for searching balances during volume runs. 0 - STARGATE_CHAINS, 1 - COREDAO_CHAINS  
    
    SRC_CHAIN_L2PASS = [27, 29] | One of the networks will be chosen (REFUEL/BRIDGE NFT(including Wormhole on Merkly))        

    DST_CHAIN_L2PASS_REFUEL = {
        1: (0.0016, 0.002), # Chain ID: (minimum, maximum) in native token of incoming network**
        2: (0.0002, 0.0005) 
    } 
    
    WORMHOLE_TOKENS_AMOUNT | Number of tokens to mint and bridge through Wormhole

    SRC_CHAIN_L2TELEGRAPH | Outgoing network for L2Telegraph
    DST_CHAIN_L2TELEGRAPH | Incoming network for L2Telegraph 
    
    L2PASS_ATTACK_REFUEL | Specify in lists the refuel option (outgoing network, incoming network, min. amount to refuel).     
    L2PASS_ATTACK_NFT    | Specify in lists the NFT bridge option (outgoing network, incoming network). 
                    
    SHUFFLE_ATTACK | If True, the software will shuffle the attack route 
    WAIT_FOR_RECEIPT | If True, the software will wait for receipt of funds in the incoming network before launching
                        the next module
    
    L2PASS_ATTACK_REFUEL = [
        ([43, 3, 0.0001], None),  # Example of using None for attack: (attack data, None).
    ]                               If None is chosen, the module will be skipped 
                                    Applies to all modules.
                                     
    L2PASS_ATTACK_REFUEL = [
        [43, [1, 2, 3], 0.0001],  # Example of using random attack: (outgoing network, list of incoming networks, amount)
    ]                               If a list of networks is specified, the module will choose one network from the list.
                                    Applies to all modules.
    
    L2PASS_GAS_STATION_DATA | Gas Station on L2Pass https://l2pass.com/gas-station. 
                              Specify in lists network and amount to refuel.

    The amount should be specified in the native token of the incoming network. Specify 10% less than the limit specified on the website,
    to avoid errors with LayerZero technology. You can check limits here: 
            1) L2Pass    - https://l2pass.com/refuel  
            2) nogem.app - https://nogem.app
            3) Merkly    - https://minter.merkly.com/gas  
            4) Whale     - https://whale-app.com/refuel
            5) Zerius    - https://zerius.io/refuel
            
"""
WAIT_FOR_RECEIPT = True     # If True, will wait for receipt of funds in the incoming network before launching the next module
ALL_DST_CHAINS = False      # If True, the refuel and bridge modules will try to make a transaction to each incoming network
L0_SEARCH_DATA = 0          # Searching balances in networks. 0 - STARGATE_CHAINS, 1 - COREDAO_CHAINS

'--------------------------------------------------Stargate / CoreDAO--------------------------------------------------'

STG_STAKE_CONFIG = [(1, 1), ('100', '100')]
STARGATE_DUST_CONFIG = (['USDV', 'USDV'], [31, 6])

STARGATE_AMOUNT = ('100', '100')
STARGATE_CHAINS = [1, 31]
STARGATE_TOKENS = ['STG', 'STG']

COREDAO_AMOUNT = ('100', '100')
COREDAO_CHAINS = [5, 11, 33]
COREDAO_TOKENS = ['USDC', 'USDC', 'USDC']

L0_BRIDGE_COUNT = 1

'--------------------------------------------------------L2Pass--------------------------------------------------------'

SRC_CHAIN_L2PASS = [6]          # Outgoing network for L2Pass
DST_CHAIN_L2PASS_NFT = [20]       # Incoming network for L2Pass Mint NFT
DST_CHAIN_L2PASS_REFUEL = {
    20: (0.6, 0.61),        # Chain ID: (minimum, maximum) in native token of incoming network (quantity)
}

'--------------------------------------------------------nogem.app-----------------------------------------------------'

SRC_CHAIN_NOGEM = [22]             # Outgoing network for nogem.app
DST_CHAIN_NOGEM_NFT = [3]       # Incoming network for nogem.app Mint NFT
DST_CHAIN_NOGEM_REFUEL = {
    3: (0.0006, 0.00061),        # Chain ID: (minimum, maximum) in native token of incoming network (quantity)
}

'--------------------------------------------------------Merkly--------------------------------------------------------'

SRC_CHAIN_MERKLY = [35]         # Outgoing network for Merkly
DST_CHAIN_MERKLY_NFT = [43]     # Incoming network for Merkly Mint NFT
DST_CHAIN_MERKLY_REFUEL = {
     3: (0.000001, 0.00002),        # Chain ID: (minimum, maximum) in native token of incoming network (quantity)
     20: (0.000001, 0.00002),        # Chain ID: (minimum, maximum) in native token of incoming network (quantity)
}

'--------------------------------------------------------Whale---------------------------------------------------------'

SRC_CHAIN_WHALE = [35]          # Outgoing network for Whale
DST_CHAIN_WHALE_NFT = [7]     # Incoming network for Whale Mint NFT
DST_CHAIN_WHALE_REFUEL = {
    42: (0.0005, 0.0005),        # Chain ID: (minimum, maximum) in native token of incoming network (quantity)
}

'-------------------------------------------------------Zerius---------------------------------------------------------'

SRC_CHAIN_ZERIUS = [35]          # Outgoing network for Zerius
DST_CHAIN_ZERIUS_NFT = [7]      # Incoming network for Zerius Mint NFT
DST_CHAIN_ZERIUS_REFUEL = {
    1: (0.0001, 0.0002),        # Chain ID: (minimum, maximum) in native token of incoming network (quantity)
}

'-------------------------------------------------------Bungee---------------------------------------------------------'

SRC_CHAIN_BUNGEE = [43]          # Outgoing network for Bungee
DST_CHAIN_BUNGEE_REFUEL = {
    5: (0.0003, 0.00031),  # Chain ID: (minimum, maximum) in native token of outgoing network (quantity)
}

'---------------------------------------------------Merkly Hyperlane---------------------------------------------------'

SRC_CHAIN_MERKLY_HYPERLANE = [9]   # Outgoing network for Merkly Hyperlane
DST_CHAIN_MERKLY_HYPERLANE = [17, 28]   # Incoming network for Merkly Hyperlane
HYPERLANE_TOKENS_AMOUNT = (1, 1)   # Number of tokens to mint and bridge on Merkly through Hyperlane

'------------------------------------------------------L2Telegraph-----------------------------------------------------'

SRC_CHAIN_L2TELEGRAPH = [41]    # Outgoing network for L2Telegraph.
DST_CHAIN_L2TELEGRAPH = [33]     # Incoming network for L2Telegraph.

'------------------------------------------------LAYERZERO REFUEL ATTACKS----------------------------------------------'

SHUFFLE_ATTACK = True      # If True, will shuffle the route for Refuel attack before start
SHUFFLE_NFT_ATTACK = True  # If True, will shuffle the route for NFT attack before start

L2PASS_ATTACK_REFUEL = [
    [43, [1, 2, 3], 0.0001],  # Example of different incoming networks
    [33, 5, 0.0001],
]

NOGEM_ATTACK_REFUEL = [
    ([43, 3, 0.0001], None),  # Example of possibility to exclude module from route
    [33, 5, 0.0001],
]

MERKLY_ATTACK_REFUEL = [
    [28, 17, 0.00001],
    [33, 5, 0.0001],
]

WHALE_ATTACK_REFUEL = [
    [28, 17, 0.00001],
    [29, 20, 0.00001],
]

ZERIUS_ATTACK_REFUEL = [
    [33, 5, 0.0001],
]

'-------------------------------------------------LAYERZERO NFT ATTACKS------------------------------------------------'

L2PASS_ATTACK_NFT = [
    [17, 18],
]

NOGEM_ATTACK_NFT = [
    [17, 18],
]

MERKLY_ATTACK_NFT = [
    [43, 3],
]

WHALE_ATTACK_NFT = [
    [17, 18],
]

ZERIUS_ATTACK_NFT = [
    [43, 3],
]

'--------------------------------------------LAYERZERO GAS STATION & FILLER--------------------------------------------'

L2PASS_GAS_STATION_ID_FROM = [33]
L2PASS_GAS_STATION_DATA = [
    ([35, 0.0000001], None),   # Example of possibility to exclude module from route
    [[34,36, 35], 0.0000001],  # Example of different incoming networks
    [34, 0.0000001],
]

NOGEM_FILLER_ID_FROM = [33]
NOGEM_FILLER_DATA = [
    ([35, 0.0000001], None),   # Example of possibility to exclude module from route
    [[34,36, 35], 0.0000001],  # Example of different incoming networks
    [34, 0.0000001],
]

"""
-----------------------------------------------------OTHER SETTINGS-----------------------------------------------------

    ZKSTARS_NFT_CONTRACTS | Specify which NFT IDs will participate in minting. All in parentheses will be used
    MINTFUN_CONTRACTS | List of contracts for minting in the selected network (GLOBAL NETWORK)
    MINTFUN_MINT_COUNT | Number of mints for MINTFUN_CONTRACTS, the software will choose a random number within the specified list 
    GRAPEGRAW_TICKETS_AMOUNT | Number of tickets to buy in one transaction on https://grapedraw.com/
    ZKSYNC_PAYMASTER_TOKEN | Specify which token you will use to pay for gas when using paymaster 
    CUSTOM_SWAP_DATA | ('token to exchange', 'token to receive', (amount from and to), launch network(see OMNI-CHAIN)), 
                        you can specify networks as a list - [1, 2, 3], then the network with the largest balance 
                        of the token to exchange will be chosen 
    BEBOP_MULTISWAP_AMOUNT | Amount or percentage of native token (minimum, maximum) (full_multi_swap_bebop module)
                             Amount in quantity  - (0.01, 0.02)
                             Amount in percentage  - ("10", "20") ⚠️ Values in quotes.
    
"""
FULL_CUSTOM_SWAP_UNISWAP = {
    "token1": '0x123',
    "token2": '0x123',
    "amount": ("100", "100"),
    "poolFee": 0.1  # % pool fee on the site
}

CUSTOM_SWAP_DATA = ('ETH', 'USDC', (0.0007, 0.0008), 43)

ZKSTARS_NFT_CONTRACTS = (1, 2, 3, 4)  # at 0 will mint all NFTs in random order

ZKSYNC_PAYMASTER_TOKEN = 1  # 0 - USDT, 1 - USDC, (0, 1) - random

GRAPEDRAW_TICKETS_AMOUNT = 1

MINTFUN_CONTRACTS = [
    '0xEb3805E0776180A783aD7f637e08172D40240311',
]

MINTFUN_MINT_COUNT = [1, 1]  # from and to

BEBOP_MULTISWAP_AMOUNT = ('10', '20')

"""
-------------------------------------------------GOOGLE-ROUTES CONTROL--------------------------------------------------
    Technology for saving progress for each account using Google Spreadsheets 
    With each launch, the software will take information from the Google table and settings below to generate a unique
     route for each account in the table.  
    ⚠️The number of accounts and their arrangement must be strictly the same for your Excel and Google Spreadsheets⚠️
                                                         
    DEPOSIT_CONFIG | Includes in the route for each account modules with values '1'
                     'okx_withdraw' will always be first
                     Bridges always after 'okx_withdraw'
                     'okx_deposit' and 'okx_collect_from_sub' always last
    
"""
DMAIL_COUNT = (0, 0)          # (minimum, maximum) additional transactions for Dmail
TRANSFER_COUNT = (0, 0)       # (minimum, maximum) additional transactions for transfers
COLLATERAL_COUNT = (0, 0)     # (minimum, maximum) additional transactions for enabling/disabling insurance
WRAPS_COUNT = (0, 0)          # (minimum, maximum) transactions through wrap_abuser module

MODULES_COUNT = (4, 5)         # (minimum, maximum) unprocessed modules from Google table
ALL_MODULES_TO_RUN = False     # Includes all unprocessed modules in the route
WITHDRAW_LP = False            # Includes all modules for withdrawing liquidity from DEX in the route
WITHDRAW_LANDING = False       # Includes all modules for withdrawing liquidity from lending in the route
HELP_NEW_MODULE = False        # Adds a random module when a module from the route fails
EXCLUDED_MODULES = ['swap_openocean']  # Excludes selected modules from the route. List in Classic-Routes
INCLUDED_MODULES = []          # Includes selected modules in the route. List in Classic-Routes

HELPERS_CONFIG = {
    'okx_withdraw'                        : 0,  # see CEX CONTROL
    'bingx_withdraw'                      : 0,  # see CEX CONTROL
    'binance_withdraw'                    : 0,  # see CEX CONTROL
    'bitget_withdraw'                     : 0,  # see CEX CONTROL
    'collector_eth'                       : 0,  # collecting all tokens in ETH within GLOBAL_NETWORK
    'make_balance_to_average'             : 0,  # equalizes your balances on accounts (see software instructions)
    'bridge_across'                       : 0,  # see BRIDGE CONTROL
    'bridge_bungee'                       : 0,  # see BRIDGE CONTROL
    'bridge_layerswap'                    : 0,  # see BRIDGE CONTROL
    'bridge_owlto'                        : 0,  # see BRIDGE CONTROL
    'bridge_orbiter'                      : 0,  # see BRIDGE CONTROL
    'bridge_relay'                        : 0,  # see BRIDGE CONTROL
    'bridge_rhino'                        : 0,  # see BRIDGE CONTROL
    'bridge_native'                       : 0,  # see BRIDGE CONTROL (amount from NATIVE_DEPOSIT_AMOUNT)
    'okx_deposit'                         : 0,  # depositing funds to the exchange
    'bingx_deposit'                       : 0,  # depositing funds to the exchange
    'binance_deposit'                     : 0,  # depositing funds to the exchange
    'bitget_deposit'                      : 0,  # depositing funds to the exchange
}

"""
--------------------------------------------CLASSIC-ROUTES CONTROL------------------------------------------------------

---------------------------------------------------HELPERS--------------------------------------------------------------        

    okx_withdraw                     # see CEX CONTROL
    bingx_withdraw                   # see CEX CONTROL
    binance_withdraw                 # see CEX CONTROL
    bitget_withdraw                  # see CEX CONTROL
    
    bridge_across                    # see BRIDGE CONTROL
    bridge_bungee                    # see BRIDGE CONTROL
    bridge_layerswap                 # see BRIDGE CONTROL
    bridge_nitro                     # see BRIDGE CONTROL
    bridge_owlto                     # see BRIDGE CONTROL
    bridge_orbiter                   # see BRIDGE CONTROL
    bridge_relay                     # see BRIDGE CONTROL
    bridge_rhino                     # see BRIDGE CONTROL
    bridge_native                    # see BRIDGE CONTROL
    
    rhino_recovery_funds             # withdrawal of funds from Rhino.fi, works according to your settings from BRIDGE CONTROL
    
    okx_deposit                      # depositing funds to the exchange + collecting funds from subAccounts to the main account
    bingx_deposit                    # depositing funds to the exchange + collecting funds from subAccounts to the main account
    binance_deposit                  # depositing funds to the exchange + collecting funds from subAccounts to the main account
    bitget_deposit                   # depositing funds to the exchange + collecting funds from subAccounts to the main account
        
    custom_swap                      # performs swap according to CUSTOM_SWAP_DATA setting
    swap_bridged_usdc                # performs swap of USDC.e to USDC through Uniswap for Polygon network 
    collector_eth                    # collecting all tokens on the account into ETH
    make_balance_to_average          # equalizes your balances on accounts (see CEX_BALANCER_CONFIG) 
    
    claim_rewards_bungee             # claim rewards for bridges through Socket on https://www.socketscan.io/rewards
    claim_op_across                  # claim OP for bridges through Socket on https://app.across.to/rewards
    
--------------------------------------------------OMNI-CHAIN------------------------------------------------------------            
    
    bridge_l2pass                    # bridge last NFT on L2Pass
    bridge_nogem                     # bridge last NFT on nogem.app
    bridge_merkly                    # bridge last NFT on Merkly
    bridge_whale                     # bridge last NFT on Whale
    bridge_zerius                    # bridge last NFT on Zerius
        
    refuel_l2pass                    # see OMNI-CHAIN CONTROL
    refuel_nogem                     # see OMNI-CHAIN CONTROL
    refuel_merkly                    # see OMNI-CHAIN CONTROL
    refuel_whale                     # see OMNI-CHAIN CONTROL
    refuel_zerius                    # see OMNI-CHAIN CONTROL
    refuel_bungee                    # see OMNI-CHAIN CONTROL
    
    smart_stake_stg                  # stake on Stargate. STG_STAKE_CONFIG. See OMNI-CHAIN CONTROL
    bridge_stargate                  # bridges on Stargate. STARGATE_CHAINS, STARGATE_TOKENS. See OMNI-CHAIN CONTROL
    bridge_stargate_dust             # sending dust on Stargate. See STARGATE_DUST_CONFIG and OMNI-CHAIN CONTROL
    bridge_coredao                   # bridges on CoreDAO. COREDAO_CHAINS, COREDAO_TOKENS. See OMNI-CHAIN CONTROL
    smart_random_approve             # random approve for network with largest balance from L0_SEARCH_DATA 
    
    mint_and_bridge_l2telegraph      # mint and bridge NFT through L2Telegraph. See OMNI-CHAIN CONTROL
    send_message_l2telegraph         # see OMNI-CHAIN CONTROL
    
    l2pass_refuel_attack             # Refuel attack on L2Pass. See OMNI-CHAIN CONTROL
    nogem_refuel_attack              # Refuel attack on nogem.app 
    merkly_refuel_attack             # Refuel attack on Merkly
    whale_refuel_attack              # Refuel attack on Whale
    zerius_refuel_attack             # Refuel attack on Zerius 
    
    l2pass_nft_attack                # NFT Bridge attack on L2Pass. See OMNI-CHAIN CONTROL
    nogem_nft_attack                 # NFT Bridge attack on nogem.app
    merkly_nft_attack                # NFT Bridge attack on Merkly
    whale_nft_attack                 # NFT Bridge attack on Whale
    zerius_nft_attack                # NFT Bridge attack on Zerius
    
    gas_station_l2pass               # Refuel to multiple networks with 1 transaction. see L2PASS_GAS_STATION_DATA     
    filler_nogem                     # Refuel to multiple networks with 1 transaction. see NOGEM_FILLER_DATA
    
-------------------------------------------------------HYPERLANE--------------------------------------------------------            

    bridge_hyperlane_nft     # mint and bridge NFT on Merkly through Hyperlane 
    bridge_hyperlane_token   # mint and bridge tokens on Merkly through Hyperlane 
    
---------------------------------------------------------ZKSYNC---------------------------------------------------------        

    add_liquidity_maverick           # USDC/WETH LP
    add_liquidity_mute               # USDC/WETH LP
    add_liquidity_syncswap           # USDC/WETH LP on LIQUIDITY_AMOUNT
    deposit_basilisk                 # makes deposit in lending on LIQUIDITY_AMOUNT
    deposit_eralend                  
    deposit_reactorfusion            
    deposit_zerolend                 
    enable_collateral_basilisk       # enables insurance for deposit on lending
    enable_collateral_eralend        
    enable_collateral_reactorfusion  
    swap_izumi                       # makes random token swaps on AMOUNT_PERCENT for ETH and 100% for others.
    swap_maverick                      pairs are chosen randomly, considering balance on wallet. Swaps work in
    swap_mute                          following directions: ETH -> Token, Token -> ETH. Token -> Token will not happen to
    swap_odos                          avoid problems with gas payment.
    swap_oneinch                     
    swap_openocean                   
    swap_pancake                     
    swap_rango                       
    swap_spacefi                     
    swap_syncswap
    swap_syncswap_paymaster                   
    swap_velocore                    
    swap_xyfinance                   
    swap_vesync                      
    swap_woofi                       
    swap_zkswap
    check_in_owlto                   # checkIn on https://owlto.finance/confirm
    wrap_eth                         # wrap ETH through official WETH token contract. (amount from LIQUIDITY_AMOUNT)
    unwrap_eth                       # unwrap ETH through official WETH token contract. (amount from LIQUIDITY_AMOUNT)
    grapedraw_bid                    # creating a bet on GrapeDraw https://grapedraw.com. see GRAPEDRAW_TICKETS_AMOUNT 
    vote_rubyscore                   # voting on RubyScore https://rubyscore.io 
    create_omnisea                   # creating a new NFT collection. All parameters will be random
    create_safe                      # creates a safe in GLOBAL_NETWORK
    mint_domain_ens                  # 0.003 ETH domain
    mint_domain_zns                  # 0.003 ETH domain
    mint_mailzero                    # mint free NFT on MailZero. Only gas fee.
    mint_tevaera                     # mint 2 NFT on Tevaera. Price: 0.0003 ETH
    mint_hypercomic                  # mint NFT for completing quests on https://zk24.hypercomic.io/
    mint_zkstars                     # mint NFT on https://zkstars.io. Price: 0.0001 ETH
    deploy_contract                  # deploy your contract. Contract is in data/services/contract_data.json
    random_approve                   # random approve of random token for swap platforms 
    send_message_dmail               # sending message through Dmail to random Web2 address (mailbox)
    transfer_eth                     # transfers (TRANSFER_AMOUNT) ETH to random address
    transfer_eth_to_myself           # transfers (TRANSFER_AMOUNT) ETH to your address
    wrap_abuser                      # ETH-WETH swaps through aggregator contracts. (amount from AMOUNT_PERCENT_WRAPS)     
    withdraw_native_bridge           # withdrawal of ETH through official bridge. (amount from NATIVE_WITHDRAW_AMOUNT)
    withdraw_basilisk                # withdrawal of liquidity from lending
    withdraw_eralend                 
    withdraw_reactorfusion           
    withdraw_zerolend                
    disable_collateral_basilisk      # disabling insurance of deposit on lending
    disable_collateral_eralend       
    disable_collateral_reactorfusion 
    withdraw_liquidity_maverick      # withdraws all liquidity from USDC/WETH pool
    withdraw_liquidity_mute
    withdraw_liquidity_syncswap
    
---------------------------------------------------------BLAST----------------------------------------------------------  

    swap_thruster
    swap_bladeswap
    swap_ambient
    wrap_eth                         
    unwrap_eth                       
    check_in_owlto
    deposit_zerolend                # deposit ETH on ZeroLend
    deposit_usdb_zerolend           # deposit USDB on ZeroLend
    withdraw_zerolend               # withdrawal of ETH from ZeroLend
    withdraw_usdb_zerolend          # withdrawal of USDB from ZeroLend
    
------------------------------------------------------Polygon zkEVM-----------------------------------------------------  
    
    swap_quickswap
    swap_pancake
    swap_woofi
    swap_rango
    swap_openocean
    swap_xyfinance
    wrap_eth                         
    unwrap_eth                       
    
----------------------------------------------------------BASE----------------------------------------------------------        

    swap_pancake
    swap_uniswap
    swap_sushiswap
    swap_woofi
    swap_maverick
    swap_izumi
    swap_odos
    swap_oneinch
    swap_openocean
    swap_xyfinance
    swap_bebop
    full_multi_swap_bebop
    deposit_seamless
    withdraw_seamless
    deposit_usdbc_seamless
    withdraw_usdbc_seamless
    deposit_moonwell
    withdraw_moonwell
    enable_collateral_moonwell
    disable_collateral_moonwell
    enable_collateral_seamless
    disable_collateral_seamless
    create_safe
    mint_mintfun
    mint_zkstars
    deploy_contract
    vote_rubyscore
    random_approve
    transfer_eth                     
    transfer_eth_to_myself
    wrap_abuser
    wrap_eth                        
    unwrap_eth                                  
    send_message_dmail
    withdraw_native_bridge

----------------------------------------------------------LINEA---------------------------------------------------------        

    swap_syncswap
    swap_pancake
    swap_woofi
    swap_velocore
    swap_izumi
    swap_rango
    swap_openocean
    swap_xyfinance
    deposit_layerbank
    withdraw_layerbank
    create_omnisea
    check_in_owlto
    mint_zkstars
    deploy_contract
    vote_rubyscore
    random_approve
    transfer_eth                     
    transfer_eth_to_myself
    wrap_abuser  
    wrap_eth                      
    unwrap_eth                                 
    send_message_dmail
    withdraw_native_bridge          

---------------------------------------------------------SCROLL---------------------------------------------------------        
    
    add_liquidity_syncswap           # USDC/WETH LP on LIQUIDITY_AMOUNT
    swap_rango
    swap_ambient
    swap_zebra
    swap_sushiswap
    swap_skydrome
    swap_syncswap
    swap_spacefi
    swap_izumi
    swap_openocean
    swap_xyfinance
    swap_bebop
    full_multi_swap_bebop
    check_in_owlto
    deposit_layerbank
    withdraw_layerbank
    create_omnisea
    mint_zkstars
    deploy_contract
    vote_rubyscore
    random_approve
    transfer_eth                     
    transfer_eth_to_myself   
    send_message_dmail
    wrap_abuser
    wrap_eth                      
    unwrap_eth                               
    withdraw_native_bridge
    
----------------------------------------------------------ZORA----------------------------------------------------------        
    
    mint_mintfun
    mint_zkstars
    wrap_eth                        
    unwrap_eth                      
    transfer_eth                     
    transfer_eth_to_myself

----------------------------------------------------------NOVA----------------------------------------------------------        
    
    swap_sushiswap
    wrap_eth                        
    unwrap_eth                                         
    transfer_eth                     
    transfer_eth_to_myself
    
    Routes for real old-timers (Machine - evil).
    Select the necessary modules for interaction
    You can create any route, the software will strictly follow it. For each list, one module will be selected into
    the route, if the software selects None, it will skip this list of modules. 
    List of modules above.
    
    CLASSIC_ROUTES_MODULES_USING = [
        ['okx_withdraw'],
        ['bridge_layerswap', 'bridge_native'],
        ['swap_mute', 'swap_izumi', 'mint_domain_ens', None],
        ...
    ]
    
    Networks for working with different projects will allow you to make a route in all active networks for retro.
    Example of filling (networks listed below):
    
    CLASSIC_ROUTES_MODULES_USING = [
        ['swap_syncswap:3'], # after the ':' character, the network number for work
    ]

    Arbitrum = 1            Scroll = 8
    Arbitrum Nova = 2       Starknet = 9
    Base = 3                Polygon ZKEVM = 10
    Linea = 4               zkSync Era = 11
    Manta = 5               Zora = 12
    Polygon = 6             Ethereum = 13
    Optimism = 7            Blast = 49
    
"""

CLASSIC_WITHDRAW_DEPENDENCIES = False  # when True after each module to add liquidity to lending, it will withdraw it

CLASSIC_ROUTES_MODULES_USING = [
    # DEX swaps (in cycles to minimize loss)
    ['swap_pancake'],  # ETH → Token
    ['swap_pancake'],  # Token → ETH
    
    ['swap_uniswap'],  # ETH → Token
    ['swap_uniswap'],  # Token → ETH
    
    ['swap_sushiswap'],  # ETH → Token
    ['swap_sushiswap'],  # Token → ETH
    
    ['swap_woofi'],  # ETH → Token
    ['swap_woofi'],  # Token → ETH
    
    ['swap_izumi'],  # ETH → Token
    ['swap_izumi'],  # Token → ETH
    
    # Alternative DEX options
    ['swap_bebop'],
    ['swap_xyfinance'],
        
    # Messaging and voting
    ['send_message_dmail'],
    ['vote_rubyscore'],
]
