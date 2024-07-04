# Kubernetes Event Dataset

This repository contains the dataset presented in [1], as well as source files used to generate and process it.

## Files
- `raw-audit-logs.log` contains raw Kubernetes audit logs collected using the `audit-policy.yaml` audit policy.
- `audit-logs.csv` contains the processed Kubernetes audit logs using Logstash.
- `events-dataset.txt` contains the processed Kubernetes logs containing only event names.

If you wish to collect your own dataset, we include several source files that might help:
- `collect.py` is a script to trigger the installation and uninstallation of public Helm repositories.
- `logstash.conf` is the Logstash configuration used to process raw audits into a more usable `audit-logs.csv`.
- `parse.py` is to process and parse the audits logs from `audit-logs.csv` to `event-dataset.txt`.
- `helm-charts.json` is a backup of Helm charts used at the time of the collection.

Extra files:
- `distribution.ipynb` is a Python Notebook to print the distribution of the event dataset. It generates a `dataset_distribution.pdf` figure.

## Reference
Please cite this dataset in your publication if it helps your research:

```
@article{kermabon2024perfspec,
  author={Kermabon-Bobinnec, Hugo and Bagheri, Sima and GholipourChoubeh, Mahmood and Majumdar, Suryadipta and Jarraya, Yosr and Wang, Lingyu and Pourzandi, Makan},
  journal={IEEE Transactions on Dependable and Secure Computing}, 
  title={PerfSPEC: Performance Profiling-based Proactive Security Policy Enforcement for Containers}, 
  year={2024},
  volume={},
  number={},
  pages={1-18},
  doi={10.1109/TDSC.2024.3420712}}

```

[1]: H. Kermabon-Bobinnec et al., "PerfSPEC: Performance Profiling-based Proactive Security Policy Enforcement for Containers," in IEEE Transactions on Dependable and Secure Computing, doi: 10.1109/TDSC.2024.3420712.