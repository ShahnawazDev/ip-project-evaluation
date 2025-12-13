import pandas as pd

# Read the CSV file, skipping the first empty row
df = pd.read_csv('results_all.csv', skiprows=1)

# Rename Total to regular total
df.rename(columns={'Total': 'regular total'}, inplace=True)

# Recalculate regular total from components
component_columns = ['Data Collection', 'Schedule Logic', 'Journey Planner', 'Code quality', 'Documentation']
df['regular total'] = df[component_columns].sum(axis=1)

# Add new column total (including bonus) = regular total + Bonus(Extensions)
df['total (including bonus)'] = df['regular total'] + df['Bonus(Extensions)']

# Reorder columns to place the new column right after regular total
col_order = list(df.columns)
# Remove the new column from its current position
new_col = col_order.pop(col_order.index('total (including bonus)'))
# Insert it right after regular total
col_order.insert(col_order.index('regular total') + 1, new_col)
df = df[col_order]

# Write back to CSV with the empty first row
with open('results_all.csv', 'w', newline='', encoding='utf-8') as f:
    # Write the empty first row
    f.write(',' * 13 + '\n')
    # Write the dataframe
    df.to_csv(f, index=False)

print('Done! Updated CSV file.')
print(f"Columns: {list(df.columns)}")
print(f"\nSample data:")
print(df[['Name', 'regular total', 'total (including bonus)', 'Bonus(Extensions)']].head())
