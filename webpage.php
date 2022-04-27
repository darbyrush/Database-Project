<head>
<title>Cryptocurrency Investment Tracker</title>
</head>
<body>

<h1>Cryptocurrency Investment Tracker</h1><br>
<p>Developed by Darby Rush and Austin Flynn</p>
<br>
<br>


<!-- functions to show forms -->
<script type="text/javascript">

    function showForm() {
        document.getElementById('formElement').style.display = 'block';
    }

    function showForm1() {
        document.getElementById('formElement1').style.display = 'block';
    }

    function showForm2() {
        document.getElementById('formElement2').style.display = 'block';
    }

    function showForm3() {
        document.getElementById('formElement3').style.display = 'block';
    }

</script>

<button onclick="showForm()">Add an Investor</button>
<button onclick="showForm1()">Add a Cryptocurrency</button>
<button onclick="showForm2()">Buy an Investment</button>
<button onclick="showForm3()">Sell an Investment</button>
<button>View all Investments</button>
<button>View all Investors</button>

<!-- Add investor form -->
<form id="formElement" style="display: none;">
    <label for="InvestorID">Investor ID:</label><br>
    <input type="text" id="InvestorID" name="InvestorID"><br>
    <label for="Name">Name:</label><br>
    <input type="text" id="Name" name="Name"><br>
    <label for="Email">Email:</label><br>
    <input type="text" id="Email" name="Email"><br>
    <input name="add_inv" type="submit" value="Submit">
</form>

<!-- Add Crypto form -->
<form id="formElement1" style="display: none;">
    <label for="CryptocurrencyID">Cryptocurrency ID:</label><br>
    <input type="text" id="CryptocurrencyID" name="CryptocurrencyID"><br>
    <label for="CryptoName">Name:</label><br>
    <input type="text" id="CryptoName" name="CryptoName"><br>
    <label for="CurrentValue">Current Value:</label><br>
    <input type="text" id="CurrentValue" name="CurrentValue">
    <input name="add_crypto" type="submit" value="Submit">
    </form>

<!-- Buy investment form -->
<form id="formElement2" style="display: none;">
    <label for="InvestorID">Investor ID:</label><br>
    <input type="text" id="InvestorID" name="InvestorID"><br>
    <label for="CryptocurrencyID">Cryptocurrency ID:</label><br>
    <input type="text" id="CryptocurrencyID" name="CryptocurrencyID"><br>
    <label for="NumShares">Number of Shares:</label><br>
    <input type="text" id="NumShares" name="fname"><br>
    <label for="PurchasePrice">Purchase Price:</label><br>
    <input type="text" id="PurchasePrice" name="PurchasePrice"><br>
    <input name="buy" type="submit" value="Submit">
    </form>

<!-- Sell investment form -->
<form id="formElement3" style="display: none;">
    <label for="SellName">Name:</label><br>
    <input type="text" id="SellName" name="SellName"><br>
    <label for="SellNumShares">Number of shares:</label><br>
    <input type="text" id="SellNumShares" name="SellNumShares"><br>
    <label for="SellPrice">Sell Price:</label><br>
    <input type="text" id="SellPrice" name="SellPrice">
    <input name="sell" type="submit" value="Submit">
    </form>

</body>

<?php

if (isset($_POST['add_inv'])){

    $InvestorID = escapeshellarg($_POST[InvestorID]);
    $name = escapeshellarg($_POST[Name]);
    $email = escapeshellarg($_POST[Email]);

    $command = 'python3 addInv.py ' . $InvestorID . ' ' . $Name . ' ' . $Email;

    $escaped_command = escapeshellcmd($command);

    system($escaped_command);
}

if (isset($_POST['add_crypto'])){

    $CryptocurrencyID = escapeshellarg($_POST[CryptocurrencyID]);
    $CryptoName = escapeshellarg($_POST[CryptoName]);
    $CurrentValue = escapeshellarg($_POST[CurrentValue]);

    $command = 'python3 addInvestor.py ' . $CryptocurrencyID . ' ' . $CryptoName . ' ' . $CurrentValue;

    $escaped_command = escapeshellcmd($command);

    system($escaped_command);
}

if (isset($_POST['buy'])){

    $InvestorId = escapeshellarg($_POST[InvestorId]);
    $CryptocurrencyId = escapeshellarg($_POST[CryptocurrencyId]);
    $NumShares = escapeshellarg($_POST[NumShares]);
    $PurchasePrice = escapeshellarg($_POST[PurchasePrice]);

    $command = 'python3 addInvestor.py ' . $InvestorId . ' ' . $CryptocurrencyId . ' ' . $NumShares . ' ' . $PurchasePrice;

    $escaped_command = escapeshellcmd($command);

    system($escaped_command);
}

if (isset($_POST['sell'])){

    $SellName = escapeshellarg($_POST[SellName]);
    $SellNumShares = escapeshellarg($_POST[SellNumShares]);
    $SellPrice = escapeshellarg($_POST[SellPrice]);

    $command = 'python3 addInvestor.py ' . $SellName . ' ' . $SellNumShares . ' ' . $SellPrice;

    $escaped_command = escapeshellcmd($command);

    system($escaped_command);
}
?>