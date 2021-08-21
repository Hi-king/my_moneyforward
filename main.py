from typing import Dict, List, Any, Union, Hashable

import fire
import moneyforward.moneyforward
import dateutil.parser
import dateutil.relativedelta
import yaml


def main(from_date, to_date):
    config: Dict = yaml.load(open("config.yaml"), Loader=yaml.SafeLoader)

    mf = moneyforward.moneyforward.MoneyForward(config)
    from_date = dateutil.parser.parse(from_date)
    to_date = dateutil.parser.parse(to_date)
    day = from_date
    mf.download_csv(year=day.year, month=day.month)
    while day < to_date:
        day += dateutil.relativedelta.relativedelta(months=1)
        mf.download_csv(year=day.year, month=day.month)


if __name__ == '__main__':
    fire.Fire(main)
