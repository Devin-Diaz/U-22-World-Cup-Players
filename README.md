# U-22-World-Cup-Players

A mini terminal like application displaying U-22 players at the FIFA World Cup 2026.

## Extra Details & Learning Processes:

Data ETL was done through Python. Initial player dataset was constructed from 
[FIFA's official Squad's List](https://fdp.fifa.org/assetspublic/ce281/pdf/SquadLists-English.pdf). Data was extracted via
[pdfplumber library](https://github.com/jsvine/pdfplumber) then filtered through basic Python logic. 

Additional data added to dataset was APIs that lead to a player's flag image from their respective nation, and color details of the flag. Flag color
details were derived from [this flag colors json file](https://github.com/reimertz/flag-colors/blob/master/data/flagColors.json). Then to
construct the API for a nation's flag I referenced [this flag code json file](https://flagcdn.com/en/codes.json) to my initial player dataset and adhered
to [Flag's API](https://flagsapi.com/) url structure to create the API. Lastly I referenced my initial player dataset, constructed flag url api, and color details from
player's flag to ensure each player/row was was coordinated with the proper data.

Lastly all through local json, I presented records in a grid like format via react.js.

TBD: Mini Backend for querying & and other fun details.
