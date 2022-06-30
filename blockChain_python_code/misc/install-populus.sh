virtualenv -p python3.6 populus-venv
source populus-venv/bin/activate
pip install eth-abi==1.2.2
pip install eth-typing==1.1.0
pip install py-ecc==1.4.7
pip install py-evm==0.2.0a33
pip install web3==4.7.2
pip install -e git+https://github.com/ethereum/populus@2ab03fea0d0e2881c80698d2a349a74cc6c953d3#egg=populus
pip install vyper
mkdir populus-project
cd populus-project
populus init
cp ../populus-venv/src/populus/populus/assets/defaults.v9.config.json project.json
cd ../populus-venv/src/populus
wget https://patch-diff.githubusercontent.com/raw/ethereum/populus/pull/484.patch
git apply 484.patch
cd ../../../populus-project
