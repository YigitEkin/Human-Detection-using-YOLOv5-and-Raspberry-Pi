## pre-setup

before running the service files, you have to install the dependencies.
you can install them using pip.

in order to check whether pip is installed or not you can execute `python3 -m pip --version`
you should see an output like this
```bash
pip 22.3.1 from /home/ubuntu/.local/lib/python3.8/site-packages/pip (python 3.8)
```
if not, make sure to install pip first [see](https://pip.pypa.io/en/stable/installation/)

after installing pip. install the dependencies for the service files by executing:

```bash
cd backend && pip install -r requirements.txt
cd ../pi_cctv_camera && pip install -r requirements.txt
```

## in order to run services execute the following commands:

```bash
cd services
systemctl daemon-reload
systemctl enable backend.service
systemctl enable pi_camera.service
systemctl start backend.service
systemctl start pi_camera.service
```

## You can check if the setup is correct by typing

```bash
systemcl status backend.service
systemcl status pi_camera.service
```
