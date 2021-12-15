# SHA256 cracking code for geocaching treasure
### Reference
https://www.geocaching.com/geocache/GC911NM

https://docs.google.com/document/d/1US305gdN7ShrDXSw6_BdtVvWtgJeDE1902sfw9kkTUI/edit#

### Requirements
```
sudo apt install python3
```

```
sudo apt install python3-pip
```

```
pip install ray
```
### Execute
First make sure to edit the variables in "sha256.py" and adjust them as needed. (Start/stop/coordinates in the for loops)
```
python3 sha256.py
```
You can use the "idcalc.py" script to find out letter combination ID. Example: AA01
```
python3 idcalc.py
```
