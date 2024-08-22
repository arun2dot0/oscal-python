
### OSCAL Demo for Containers
OSCAL (Open Security Controls Assessment Language) is a standardized framework developed by 
NIST (National Institute of Standards and Technology) in collaboration with FedRAMP 
to digitize and automate security authorization processes

### Buisness need
Automate Security Assessment and Auditing Process as the standardized
formats are machine-readable .Easier sharing of security assessment and 
control implementation details between parties.

### How to use for Containers

Scan any image and generate the Vulnerability report . I am using
trivy scan to get the scan output as JSON

```commandline

trivy image  --format json --output results.json  hello-world-scala:1.0 
```
_Note: I have included the results.json as a sample , but you can generate your own_


### Converting to Image Vulnerabilities to OSCAN format
Now we will convert the results to OSCAL using Python using pydantic library . 
I am using Python 3.11 

```
pip install pydantic
pip install 'pydantic[email]'
pip install email-validator
```

Then execute
```
python3 oscal.py
```
