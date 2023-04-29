# Define the FQDN to check
$fqdn = $args[0]
$fqdn_type = $args[1]

# Define the DNS servers to check against
$nameservers = @(
    "dns1.p01.nsone.net",
    "dilbert.ns.cloudflare.com"
)

# Define the ANSI color codes for the output
$red = [console]::ForegroundColor = "Red"
$orange = [console]::ForegroundColor = "DarkYellow"
$yellow = [console]::ForegroundColor = "Yellow"
$green = [console]::ForegroundColor = "Green"
$reset = [console]::ResetColor()

# Loop through the DNS servers and check the resolution of the FQDN
foreach ($ns in $nameservers) {
    Write-Host "Checking $fqdn on $ns..."

    # Resolve the FQDN using the current DNS server
    $result = nslookup $fqdn $ns | Select-String -Pattern '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' | Select-Object -First 1
    $result = $result.ToString().Trim()

    # Compare the resolution to the first result (if any)
    if ([string]::IsNullOrEmpty($result)) {
        Write-Host "Unable to resolve $fqdn on $ns"
        continue
    }
    elseif ([string]::IsNullOrEmpty($expected)) {
        $expected = $result
        continue
    }
    elseif ($result -eq $expected) {
        Write-Host -ForegroundColor $green "OK" $reset
        Write-Host $result
    }
    elseif ($result -like "*$expected*") {
        Write-Host -ForegroundColor $yellow "Similar" $reset
    }
    elseif ($result -notlike "*$expected*") {
        Write-Host -ForegroundColor $orange "Different" $reset
        Write-Host "Expected: $expected"
        Write-Host "Actual: $result"
    }
}

# Check if there were any strictly different results
foreach ($ns in $nameservers) {
    $result = nslookup $fqdn $ns | Select-String -Pattern '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' | Select-Object -First 1
    $result = $result.ToString().Trim()
    if ($result -ne $expected) {
        Write-Host -ForegroundColor $red "Strictly Different Result Detected On $ns!" $reset
        Write-Host "Expected: $expected"
        Write-Host "Actual: $result"
        exit 1
    }
}
