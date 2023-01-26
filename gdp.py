{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a20a9168",
   "metadata": {},
   "outputs": [],
   "source": [
    "from fredapi import Fred \n",
    "fred = Fred(api_key='d837251519348a565319f8cf14a42786')\n",
    "gdp = fred.get_series('MKTGDPRUA646NWDB', observation_start='1998-1-1')\n",
    "gdp.to_csv('/Users/unghwanahn/git/gdp.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf4d000b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
