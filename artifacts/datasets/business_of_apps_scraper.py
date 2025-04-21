from bs4 import BeautifulSoup
import os
import pandas as pd
FOLDER = "business_of_apps"
if __name__ == "__main__":
    

    for file in os.listdir(FOLDER):
        dataframes = {}
        

        filename = os.path.join(FOLDER, file)

        with open(filename, "r", encoding="iso-8859-1") as f:
            html = f.read()

        # parses the html with soup
        soup = BeautifulSoup(html, "html.parser")

        # extracts all the tables from the website
        tables = soup.find_all("table")

        # removes the first info table (not using)
        tables = tables[1:]

        name = file.split(".")[0]

        print(name)

        for table in tables:
            headers = []
            
            # gets the table name
            label = table["aria-label"]
            
            print(label)
            rows = table.find_all("tr")
            # gets the column headers
            top_row = rows[0]
            for header in top_row.find_all("th"):
                headers.append(header.text.strip())

            data_rows = []
            bottom_rows = rows[1:]

            for row in bottom_rows:
                cells = [td.text.strip() for td in row.find_all("td")]
                if cells:
                    data_rows.append(cells)
                else:
                    cells = [td.text.strip() for td in row.find_all("th")]
                    if cells:
                        data_rows.append(cells)

            df = pd.DataFrame(data_rows, columns=headers)
            
            dataframes[label] = df

        print(dataframes.keys())

        
    
        with pd.ExcelWriter(f"{FOLDER}_{name}.xlsx", engine='xlsxwriter') as writer:
            for df in dataframes:
                if len(df) > 31:
                    sheet_name = df[:31]
                else:
                    sheet_name = df
                dataframes[df].to_excel(writer, sheet_name=sheet_name, index=False)

            

            
            