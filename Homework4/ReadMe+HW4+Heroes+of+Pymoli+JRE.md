

```python
# Homework 4 Pandas - Option 1: Heroes of Pymoli

# Analyzing the data for the fantasy game Heroes of Pymoli.
# Like many others in its genre, the game is free-to-play, but players are
# encouraged to purchase optional items that enhance their playing experience. 

# Imports
import pandas as pd
import numpy as np

```


```python
# input files
# Save path to data set in a variable
Purch_data_file1 = "HeroesOfPymoli/Purchase_data.json"
Purch_data_file2 = "HeroesOfPymoli/Purchase_data2.json"

CurrentFile_df = pd.read_json(Purch_data_file1)
CurrentFile_df.head()

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
CurrentFile_df.columns
```




    Index(['Age', 'Gender', 'Item ID', 'Item Name', 'Price', 'SN'], dtype='object')




```python
#Player Count
# -Total Number of Players
TotalPlayers = CurrentFile_df['SN'].value_counts().count()
print("Player Count")
print("   * Total Number of Players:  " + str(TotalPlayers))
print(" ")
```

    Player Count
       * Total Number of Players:  573
     
    


```python
#Purchasing Analysis (Total)
# -Number of Unique Items
# -Average Purchase Price
# -Total Number of Purchases
# -Total Revenue
UniqueItems = CurrentFile_df['Item ID'].value_counts().count()
PurchaseCount = CurrentFile_df['Item ID'].count()
#PopItemOutputTable['Ave Purch Price'] = PopItemOutputTable['Ave Purch Price'].map("${:.2f}".format)
#TotalRev = CurrentFile_df['Price'].sum().map("${:.2f}".format)
TotalRev = CurrentFile_df['Price'].sum()
TotalRev = round(TotalRev, 2)
AvgPrice = CurrentFile_df['Price'].mean()
AvgPrice = round(AvgPrice, 2)
#AvgPrice = AvgPrice.map
print("Purchasing Analysis")
print("   * Number of Unique Items:  " + str(UniqueItems))
print("   * Average Purchase Price:  " + str(AvgPrice))
print("   * Total Number of Purchases:  " + str(PurchaseCount))
print("   * Total Revenue:  " + str(TotalRev))
print(" ")
```

    Purchasing Analysis
       * Number of Unique Items:  183
       * Average Purchase Price:  2.93
       * Total Number of Purchases:  780
       * Total Revenue:  2286.33
     
    


```python
#Gender Demographics
# •	Percentage and Count of Male Players
# •	Percentage and Count of Female Players
# •	Percentage and Count of Other / Non-Disclosed

MalePlayer_df= CurrentFile_df.loc[CurrentFile_df['Gender'] == 'Male',:]
#MalePlayer_df.head()
MalePlayers = MalePlayer_df['SN'].value_counts().count()
FemalePlayer_df= CurrentFile_df.loc[CurrentFile_df['Gender'] == 'Female',:]
FemalePlayers = FemalePlayer_df['SN'].value_counts().count()
OtherPlayers = (TotalPlayers - MalePlayers - FemalePlayers)
PercentOther = (OtherPlayers / TotalPlayers)
PercentMale = (MalePlayers / TotalPlayers)
PercentFemale = (FemalePlayers / TotalPlayers)
PercentFemale = round(PercentFemale, 2) *100
PercentOther = round(PercentOther, 2) *100
PercentMale = round(PercentMale, 2) *100
print("Gender Demographics")
print("   * Total Number of Players:  " + str(TotalPlayers))
print("   * Total Number of Male Players:  " + str(MalePlayers))
print("   * Percent Male Players:  " + str(PercentMale) + "%")
print("   * Total Number of Female Players:  " + str(FemalePlayers))
print("   * Percent Female Players:  " + str(PercentFemale) + "%")
print("   * Total Number of Other Players:  " + str(OtherPlayers))
print("   * Percent Other Players:  " + str(PercentOther) + "%")
print(" ")
```

    Gender Demographics
       * Total Number of Players:  573
       * Total Number of Male Players:  465
       * Percent Male Players:  81.0%
       * Total Number of Female Players:  100
       * Percent Female Players:  17.0%
       * Total Number of Other Players:  8
       * Percent Other Players:  1.0%
     
    


```python
#Purchasing Analysis (Gender)
# The below each broken by gender
# o Purchase Count
# o Average Purchase Price
# o Total Purchase Value
# o Normalized Totals

PurchCntM = MalePlayer_df['SN'].count()
PurchCntF = FemalePlayer_df['SN'].count()
PurchDollarM = MalePlayer_df['Price'].sum()
AvePurchPriceM = PurchDollarM / PurchCntM
AvePurchPriceM = round(AvePurchPriceM, 2)
PurchDollarF = FemalePlayer_df['Price'].sum()
AvePurchPriceF = PurchDollarF / PurchCntF
AvePurchPriceF = round(AvePurchPriceF, 2)
PurchCntO = PurchaseCount - PurchCntF - PurchCntM
PurchDollarO = TotalRev - PurchDollarF - PurchDollarM
AvePurchPriceO = PurchDollarO / PurchCntO
AvePurchPriceO = round(AvePurchPriceO, 2)
NmlzedPurchCntM = round((PurchCntM / PurchaseCount * 100), 2)
NmlzedPurchCntF = round((PurchCntF / PurchaseCount * 100), 2)
NmlzedPurchCntO = 100 - (NmlzedPurchCntM + NmlzedPurchCntF)
NmlzedPurchaseDollarM = round((PurchDollarM / TotalRev *100), 2)
NmlzedPurchaseDollarF = round((PurchDollarF / TotalRev * 100), 2)
NmlzedPurchaseDollarO = round(100 - (NmlzedPurchaseDollarF + NmlzedPurchaseDollarM), 2)
PurchDollarM = round(PurchDollarM, 2)
PurchDollarF = round(PurchDollarF, 2)
PurchDollarO = round(PurchDollarO, 2)

print("Purchasing Analysis (Gender)")
#         Item     Male     Female
print("   * Purchase Count (M/F/Other):  " + str(PurchCntM) + " " + str(PurchCntF) + " " + str(PurchCntO))
print("   * Average Purchase Price (M/F/Other):  " + "$" + str(AvePurchPriceM) + " $" + str(AvePurchPriceF) + " $" + str(AvePurchPriceO))
print("   * Total Purchase Value (M/F/Other):  $" + str(PurchDollarM) + " $" + str(PurchDollarF) + " $" + str(PurchDollarO))
print("Normalized Totals:  Purchase Count")
print("   * Purchase Count - Females percent of purchase transactions:  " + str(NmlzedPurchCntF) + "%")
print("   * Purchase Count - Males percent of purchase transactions:  " + str(NmlzedPurchCntM) + "%")
print("   * Purchase Count - Other / Unknown percent of purchase transactions:  " + str(NmlzedPurchCntO)+ "%")
print("Normalized Totals:  Purchase Amount")
print("   * Purchase Amount - Females percent of purchase dollars:  " + str(NmlzedPurchaseDollarF) + "%")
print("   * Purchase Amount - Males percent of purchase dollars:  " + str(NmlzedPurchaseDollarM) + "%")
print("   * Purchase Amount - Other / Unknown percent of purchase dollars:  " + str(NmlzedPurchaseDollarO) + "%")
print(" ")
#MalePlayer_df.head() 

```

    Purchasing Analysis (Gender)
       * Purchase Count (M/F/Other):  633 136 11
       * Average Purchase Price (M/F/Other):  $2.95 $2.82 $3.25
       * Total Purchase Value (M/F/Other):  $1867.68 $382.91 $35.74
    Normalized Totals:  Purchase Count
       * Purchase Count - Females percent of purchase transactions:  17.44%
       * Purchase Count - Males percent of purchase transactions:  81.15%
       * Purchase Count - Other / Unknown percent of purchase transactions:  1.41%
    Normalized Totals:  Purchase Amount
       * Purchase Amount - Females percent of purchase dollars:  16.75%
       * Purchase Amount - Males percent of purchase dollars:  81.69%
       * Purchase Amount - Other / Unknown percent of purchase dollars:  1.56%
     
    


```python
#Age Demographics
# The below each broken into bins of 4 years (i.e. <10, 10-14, 15-19, etc.)
# o Purchase Count
# o Average Purchase Price
# o Total Purchase Value
# o Normalized Totals

# Create the bins in which Data will be held
# Bins are 0 to 10, 10 to 14, 15 to 19, 20 to 24, 25 to 29, etc
demo_bins = [0, 10, 15, 20, 25, 30, 131]
# Create the names for the four bins
demo_group_names = ['<10', '10-14', '15-19', '20-24', '25-29', '30 and over']
```


```python
# Cut CurrentFile_df and place the ages into bins
#  pd.cut(CurrentFile_df["Age"], demo_bins, labels=demo_group_names)
CurrentFile_df["Age Demographic"] = pd.cut(CurrentFile_df["Age"], demo_bins, labels=demo_group_names)
CurrentFile_df.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age Demographic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
      <td>30 and over</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
      <td>30 and over</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
      <td>20-24</td>
    </tr>
  </tbody>
</table>
</div>




```python
DemoUnder10_df = CurrentFile_df.loc[CurrentFile_df['Age Demographic'] == '<10',:]
Demo1014_df = CurrentFile_df.loc[CurrentFile_df['Age Demographic'] == '10-14',:]
Demo1519_df = CurrentFile_df.loc[CurrentFile_df['Age Demographic'] == '15-19',:]
Demo2024_df = CurrentFile_df.loc[CurrentFile_df['Age Demographic'] == '20-24',:]
Demo2529_df = CurrentFile_df.loc[CurrentFile_df['Age Demographic'] == '25-29',:]
Demo30plus_df = CurrentFile_df.loc[CurrentFile_df['Age Demographic'] == '30 and over',:]
#PurcHCntDemo30plus_df.head(11)

# Purchase Counts
PurchCntUnder10 = DemoUnder10_df['Item ID'].count()
PurchCnt1014 = Demo1014_df['Item ID'].count()
PurchCnt1519 = Demo1519_df['Item ID'].count()
PurchCnt2024 = Demo2024_df['Item ID'].count()
PurchCnt2529 = Demo2529_df['Item ID'].count()
PurchCntOver30 = Demo30plus_df['Item ID'].count()

#Purchase Amount
PurchRevUnder10 = round(DemoUnder10_df['Price'].sum(), 2)
PurchRev1014 = round(Demo1014_df['Price'].count(),2)
PurchRev1519 = round(Demo1519_df['Price'].sum(), 2)
PurchRev2024 = round(Demo2024_df['Price'].sum(), 2)
PurchRev2529 = round(Demo2529_df['Price'].sum(), 2)
PurchRevOver30 = round(Demo30plus_df['Price'].sum(), 2)

# Average Purchase
AveUnder10 = round((PurchRevUnder10 / PurchCntUnder10), 2)
Ave1014 = round((PurchRev1014 / PurchCnt1014), 2)
Ave1519 = round((PurchRev1519 / PurchCnt1519), 2)
Ave2024 = round((PurchRev2024 / PurchCnt2024), 2)
Ave2529 = round((PurchRev2529 / PurchCnt2529), 2)
AveOver30 = round((PurchRevOver30 / PurchCntOver30), 2)

#Normalized %
#Purchase count
NPCUnder10 = round(((PurchCntUnder10 / PurchaseCount) * 100), 2)
NPC1014 = round(((PurchCnt1014 / PurchaseCount) * 100), 2)
NPC1519 = round(((PurchCnt1519 / PurchaseCount) * 100), 2)
NPC2024 = round(((PurchCnt2024 / PurchaseCount) * 100), 2)
NPC2529 = round(((PurchCnt2529 / PurchaseCount) * 100), 2)
NPCOver30 = round(((PurchCntOver30 / PurchaseCount) * 100), 2)

#Revenue
NRUnder10 = round(((PurchRevUnder10 / TotalRev) * 100), 2)
NR1014 = round(((PurchRev1014 / PurchaseCount) * 100), 2)
NR1519 = round(((PurchRev1519 / PurchaseCount) * 100), 2)
NR2024 = round(((PurchRev2024 / PurchaseCount) * 100), 2)
NR2529 = round(((PurchRev2529 / PurchaseCount) * 100), 2)
NROver30 = round(((PurchRevOver30 / PurchaseCount) * 100), 2)

# Print the results
#  Purchase Count
print("Purchase Counts by Age Demographic")
print("Under 10:  " + str(PurchCntUnder10))
print("   10-14:  " + str(PurchCnt1014))
print("   15-19:  " + str(PurchCnt1519))
print("   20-24:  " + str(PurchCnt2024))
print("   25-29:  " + str(PurchCnt2529))
print(" Over 30:  " + str(PurchCntOver30))
print(" ")

#  Total Purchase Value
print("Purchase Revenue by Age Demographic")
print("Under 10:  $" + str(PurchRevUnder10))
print("   10-14:  $" + str(PurchRev1014))
print("   15-19:  $" + str(PurchRev1519))
print("   20-24:  $" + str(PurchRev2024))
print("   25-29:  $" + str(PurchRev2529))
print(" Over 30:  $" + str(PurchRevOver30))
print(" ")

#  Average Purchase Price
print("Average Purchase Amount by Age Demographic")
print("Under 10:  $" + str(AveUnder10))
print("   10-14:  $" + str(Ave1014))
print("   15-19:  $" + str(Ave1519))
print("   20-24:  $" + str(Ave2024))
print("   25-29:  $" + str(Ave2529))
print(" Over 30:  $" + str(AveOver30))
print(" ")

# Normalized Totals
print("Normalized for the Age Groups")
print("Under 10:  ")
print("   % of Purchase count:  " + str(NPCUnder10) + "%")
print("   % of Revenue:         " + str(NRUnder10) + "%")
print("Ages 10-14:  ")
print("   % of Purchase count:  " + str(NPC1014) + "%")
print("   % of Revenue:         " + str(NR1014) + "%")
print("Ages 15-19:  ")
print("   % of Purchase count:  " + str(NPC1519) + "%")
print("   % of Revenue:         " + str(NR1519) + "%")
print("Ages 20-24:  ")
print("   % of Purchase count:  " + str(NPC2024) + "%")
print("   % of Revenue:         " + str(NR2024) + "%")
print("Ages 25-29:  ")
print("   % of Purchase count:  " + str(NPC2529) + "%")
print("   % of Revenue:         " + str(NR2529) + "%")
print("30 and over:  ")
print("   % of Purchase count:  " + str(NPCOver30) + "%")
print("   % of Revenue:         " + str(NROver30) + "%")
print(" ")

```

    Purchase Counts by Age Demographic
    Under 10:  32
       10-14:  78
       15-19:  184
       20-24:  305
       25-29:  76
     Over 30:  105
     
    Purchase Revenue by Age Demographic
    Under 10:  $96.62
       10-14:  $78
       15-19:  $528.74
       20-24:  $902.61
       25-29:  $219.82
     Over 30:  $314.39
     
    Average Purchase Amount by Age Demographic
    Under 10:  $3.02
       10-14:  $1.0
       15-19:  $2.87
       20-24:  $2.96
       25-29:  $2.89
     Over 30:  $2.99
     
    Normalized for the Age Groups
    Under 10:  
       % of Purchase count:  4.1%
       % of Revenue:         4.23%
    Ages 10-14:  
       % of Purchase count:  10.0%
       % of Revenue:         10.0%
    Ages 15-19:  
       % of Purchase count:  23.59%
       % of Revenue:         67.79%
    Ages 20-24:  
       % of Purchase count:  39.1%
       % of Revenue:         115.72%
    Ages 25-29:  
       % of Purchase count:  9.74%
       % of Revenue:         28.18%
    30 and over:  
       % of Purchase count:  13.46%
       % of Revenue:         40.31%
     
    


```python
#Top Spenders
# Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
# o SN
# o Purchase Count
# o Average Purchase Price
# o Total Purchase Value

# Get the items purchased counts by Screen Name
ItemCounts = CurrentFile_df['SN'].value_counts()

# Using GroupBy in order to separate the data into fields according to "SN" values
GroupedBySN_df = CurrentFile_df.groupby(['SN'])

# In order to be visualized, a data function must be used...
SumPurchased = GroupedBySN_df['Price'].sum()
AvgPurchase = SumPurchased / ItemCounts
# create an Output table
OutputTable = pd.DataFrame({'Items purchased': ItemCounts,
                            'Average Purch Amount': AvgPurchase,
                            'Total Purch Amount':SumPurchased})
OutputTable['Average Purch Amount'] = OutputTable['Average Purch Amount'].map("${:.2f}".format)
OutputTable['Total Purch Amount'] = OutputTable['Total Purch Amount'].map("${:.2f}".format)
OutputTable.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purch Amount</th>
      <th>Items purchased</th>
      <th>Total Purch Amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Adairialis76</th>
      <td>$2.46</td>
      <td>1</td>
      <td>$2.46</td>
    </tr>
    <tr>
      <th>Aduephos78</th>
      <td>$2.23</td>
      <td>3</td>
      <td>$6.70</td>
    </tr>
    <tr>
      <th>Aeduera68</th>
      <td>$1.93</td>
      <td>3</td>
      <td>$5.80</td>
    </tr>
    <tr>
      <th>Aela49</th>
      <td>$2.46</td>
      <td>1</td>
      <td>$2.46</td>
    </tr>
    <tr>
      <th>Aela59</th>
      <td>$1.27</td>
      <td>1</td>
      <td>$1.27</td>
    </tr>
  </tbody>
</table>
</div>




```python
# sort the table
OutputTable = OutputTable.sort_values('Total Purch Amount', ascending=False)
OutputTable.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purch Amount</th>
      <th>Items purchased</th>
      <th>Total Purch Amount</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Qarwen67</th>
      <td>$2.49</td>
      <td>4</td>
      <td>$9.97</td>
    </tr>
    <tr>
      <th>Sondim43</th>
      <td>$3.13</td>
      <td>3</td>
      <td>$9.38</td>
    </tr>
    <tr>
      <th>Tillyrin30</th>
      <td>$3.06</td>
      <td>3</td>
      <td>$9.19</td>
    </tr>
    <tr>
      <th>Lisistaya47</th>
      <td>$3.06</td>
      <td>3</td>
      <td>$9.19</td>
    </tr>
    <tr>
      <th>Tyisriphos58</th>
      <td>$4.59</td>
      <td>2</td>
      <td>$9.18</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Most Popular Items
# •	Identify the 5 most popular items by purchase count, then list (in a table):
# o	Item ID
# o	Item Name
# o	Purchase Count
# o	Item Price
# o	Total Purchase Value
#CurrentFile_df.head(5)

# Get the items purchased counts by Item Name
PopItemIDCounts = CurrentFile_df['Item ID'].value_counts()

# Using GroupBy in order to separate the data into fields according to "Item Name" values
GroupedByItemName_df = CurrentFile_df.groupby(['Item ID'])

# In order to be visualized, a data function must be used...
PopItemSumPurch = GroupedByItemName_df['Price'].sum()

# create an Output table
PopItemOutputTable = pd.DataFrame({'Total Purch Val' : PopItemSumPurch,
                                   'Purchase Count' : PopItemIDCounts})
PopItemOutputTable[['Total Purch Val', 'Purchase Count']] = PopItemOutputTable[['Total Purch Val', 'Purchase Count']].astype(float)
PopItemOutputTable['Ave Purch Price'] = (PopItemOutputTable['Total Purch Val'] / PopItemOutputTable['Purchase Count'])
                                  
# Format to $0.00
PopItemOutputTable['Total Purch Val'] = PopItemOutputTable['Total Purch Val'].map("${:.2f}".format)
PopItemOutputTable['Ave Purch Price'] = PopItemOutputTable['Ave Purch Price'].map("${:.2f}".format)
# sort the table
PopItemOutputTable = PopItemOutputTable.sort_values('Purchase Count', ascending=False)
PopItemOutputTable.reset_index(inplace=True)
PopItemOutputTable = PopItemOutputTable.rename(columns = {'index' : 'Item ID'})
PopItemOutputTable.head(5)

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Purchase Count</th>
      <th>Total Purch Val</th>
      <th>Ave Purch Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>39</td>
      <td>11.0</td>
      <td>$25.85</td>
      <td>$2.35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>84</td>
      <td>11.0</td>
      <td>$24.53</td>
      <td>$2.23</td>
    </tr>
    <tr>
      <th>2</th>
      <td>31</td>
      <td>9.0</td>
      <td>$18.63</td>
      <td>$2.07</td>
    </tr>
    <tr>
      <th>3</th>
      <td>175</td>
      <td>9.0</td>
      <td>$11.16</td>
      <td>$1.24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>13</td>
      <td>9.0</td>
      <td>$13.41</td>
      <td>$1.49</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create a lookup table for Item ID / Item Description
LookupItemDescr_df = CurrentFile_df
# Get rid of unneeded columns
LookupItemDescr_df = LookupItemDescr_df.drop('Age', axis=1)
LookupItemDescr_df = LookupItemDescr_df.drop('Gender', axis=1)
#LookupItemDescr_df = LookupItemDescr_df.drop('Price', axis=1)
LookupItemDescr_df = LookupItemDescr_df.drop('SN', axis=1)
LookupItemDescr_df = LookupItemDescr_df.drop('Age Demographic', axis=1)
# remove duplicate rows
LookupItemDescr__df = LookupItemDescr_df.drop_duplicates(subset=['Item ID','Item Name'])
LookupItemDescr_df.head(5)

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
    </tr>
    <tr>
      <th>1</th>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
    </tr>
    <tr>
      <th>2</th>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
    </tr>
    <tr>
      <th>3</th>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
    </tr>
    <tr>
      <th>4</th>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
    </tr>
  </tbody>
</table>
</div>




```python
# merge the tables
MergedTables = pd.merge(PopItemOutputTable, LookupItemDescr_df, on='Item ID', how='inner')
MergedTables['Price'] = MergedTables['Price'].map("${:.2f}".format)
MergedTables.head(12)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Purchase Count</th>
      <th>Total Purch Val</th>
      <th>Ave Purch Price</th>
      <th>Item Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>39</td>
      <td>11.0</td>
      <td>$25.85</td>
      <td>$2.35</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>$2.35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>39</td>
      <td>11.0</td>
      <td>$25.85</td>
      <td>$2.35</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>$2.35</td>
    </tr>
    <tr>
      <th>2</th>
      <td>39</td>
      <td>11.0</td>
      <td>$25.85</td>
      <td>$2.35</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>$2.35</td>
    </tr>
    <tr>
      <th>3</th>
      <td>39</td>
      <td>11.0</td>
      <td>$25.85</td>
      <td>$2.35</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>$2.35</td>
    </tr>
    <tr>
      <th>4</th>
      <td>39</td>
      <td>11.0</td>
      <td>$25.85</td>
      <td>$2.35</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>$2.35</td>
    </tr>
    <tr>
      <th>5</th>
      <td>39</td>
      <td>11.0</td>
      <td>$25.85</td>
      <td>$2.35</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>$2.35</td>
    </tr>
    <tr>
      <th>6</th>
      <td>39</td>
      <td>11.0</td>
      <td>$25.85</td>
      <td>$2.35</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>$2.35</td>
    </tr>
    <tr>
      <th>7</th>
      <td>39</td>
      <td>11.0</td>
      <td>$25.85</td>
      <td>$2.35</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>$2.35</td>
    </tr>
    <tr>
      <th>8</th>
      <td>39</td>
      <td>11.0</td>
      <td>$25.85</td>
      <td>$2.35</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>$2.35</td>
    </tr>
    <tr>
      <th>9</th>
      <td>39</td>
      <td>11.0</td>
      <td>$25.85</td>
      <td>$2.35</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>$2.35</td>
    </tr>
    <tr>
      <th>10</th>
      <td>39</td>
      <td>11.0</td>
      <td>$25.85</td>
      <td>$2.35</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>$2.35</td>
    </tr>
    <tr>
      <th>11</th>
      <td>84</td>
      <td>11.0</td>
      <td>$24.53</td>
      <td>$2.23</td>
      <td>Arcane Gem</td>
      <td>$2.23</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Remove Duplicates and drop Ave Price Column
#LookupItemDescr__df = LookupItemDescr_df.drop_duplicates(subset=['Item ID','Item Name'])
MergedTables = MergedTables.drop_duplicates(subset=['Item ID'])
MergedTables = MergedTables.drop('Ave Purch Price', axis=1)
MergedTables.head(5)

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Purchase Count</th>
      <th>Total Purch Val</th>
      <th>Item Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>39</td>
      <td>11.0</td>
      <td>$25.85</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>$2.35</td>
    </tr>
    <tr>
      <th>11</th>
      <td>84</td>
      <td>11.0</td>
      <td>$24.53</td>
      <td>Arcane Gem</td>
      <td>$2.23</td>
    </tr>
    <tr>
      <th>22</th>
      <td>31</td>
      <td>9.0</td>
      <td>$18.63</td>
      <td>Trickster</td>
      <td>$2.07</td>
    </tr>
    <tr>
      <th>31</th>
      <td>175</td>
      <td>9.0</td>
      <td>$11.16</td>
      <td>Woeful Adamantite Claymore</td>
      <td>$1.24</td>
    </tr>
    <tr>
      <th>40</th>
      <td>13</td>
      <td>9.0</td>
      <td>$13.41</td>
      <td>Serenity</td>
      <td>$1.49</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Most Popular Items
# •	Identify the 5 most popular items by purchase count, then list (in a table):
# o	Item ID
# o	Item Name
# o	Purchase Count
# o	Item Price
# o	Total Purchase Value
# Rearrange the columns
MergedTables = MergedTables[['Item ID', 'Item Name', 'Purchase Count', 'Price', 'Total Purch Val']]
MergedTables.head(5)
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Price</th>
      <th>Total Purch Val</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>39</td>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>11.0</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>11</th>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>11.0</td>
      <td>$2.23</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>22</th>
      <td>31</td>
      <td>Trickster</td>
      <td>9.0</td>
      <td>$2.07</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>31</th>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>9.0</td>
      <td>$1.24</td>
      <td>$11.16</td>
    </tr>
    <tr>
      <th>40</th>
      <td>13</td>
      <td>Serenity</td>
      <td>9.0</td>
      <td>$1.49</td>
      <td>$13.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Most Profitable Items
# • Identify the 5 most profitable items by total purchase value, then list (in a table):
# • Item ID
# • Item Name
# • Purchase Count
# • Item Price
# • Total Purchase Value

# Get the items purchased counts by Item Name
ProfItemIDCounts = CurrentFile_df['Item ID'].value_counts()

# Using GroupBy in order to separate the data into fields according to "Item Name" values
GroupByItemName_df = CurrentFile_df.groupby(['Item ID'])

# In order to be visualized, a data function must be used...
ProfItemSumPurch = GroupByItemName_df['Price'].sum()

# create an Output table
ProfItemOutputTable = pd.DataFrame({'Total Purch Val' : ProfItemSumPurch,
                                   'Purchase Count' : ProfItemIDCounts})
ProfItemOutputTable[['Total Purch Val', 'Purchase Count']] = ProfItemOutputTable[['Total Purch Val', 'Purchase Count']].astype(float)
ProfItemOutputTable.head(5)

# Format to $0.00
ProfItemOutputTable['Total Purch Val'] = ProfItemOutputTable['Total Purch Val'].map("${:.2f}".format)
ProfItemOutputTable.head(5)

# sort the table
ProfItemOutputTable = ProfItemOutputTable.sort_values('Total Purch Val', ascending=False)

ProfItemOutputTable.reset_index(inplace=True)
ProfItemOutputTable = ProfItemOutputTable.rename(columns = {'index' : 'Item ID'})
ProfItemOutputTable.head(5)

# merge the tables
MergedProfTables = pd.merge(ProfItemOutputTable, LookupItemDescr_df, on='Item ID', how='inner')
MergedProfTables['Price'] = MergedProfTables['Price'].map("${:.2f}".format)


# Remove Duplicates
MergedProfTables = MergedProfTables.drop_duplicates(subset=['Item ID'])
MergedProfTables = MergedProfTables[['Item ID', 'Item Name', 'Purchase Count', 'Price', 'Total Purch Val']]
MergedProfTables.head(12)


```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Purchase Count</th>
      <th>Price</th>
      <th>Total Purch Val</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>170</td>
      <td>Shadowsteel</td>
      <td>5.0</td>
      <td>$1.98</td>
      <td>$9.90</td>
    </tr>
    <tr>
      <th>5</th>
      <td>21</td>
      <td>Souleater</td>
      <td>3.0</td>
      <td>$3.27</td>
      <td>$9.81</td>
    </tr>
    <tr>
      <th>8</th>
      <td>37</td>
      <td>Shadow Strike, Glory of Ending Hope</td>
      <td>5.0</td>
      <td>$1.93</td>
      <td>$9.65</td>
    </tr>
    <tr>
      <th>13</th>
      <td>127</td>
      <td>Heartseeker, Reaver of Souls</td>
      <td>3.0</td>
      <td>$3.21</td>
      <td>$9.63</td>
    </tr>
    <tr>
      <th>16</th>
      <td>120</td>
      <td>Agatha</td>
      <td>5.0</td>
      <td>$1.91</td>
      <td>$9.55</td>
    </tr>
    <tr>
      <th>21</th>
      <td>96</td>
      <td>Blood-Forged Skeletal Spine</td>
      <td>2.0</td>
      <td>$4.77</td>
      <td>$9.54</td>
    </tr>
    <tr>
      <th>23</th>
      <td>47</td>
      <td>Alpha, Reach of Ending Hope</td>
      <td>6.0</td>
      <td>$1.55</td>
      <td>$9.30</td>
    </tr>
    <tr>
      <th>29</th>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>4.0</td>
      <td>$2.32</td>
      <td>$9.28</td>
    </tr>
    <tr>
      <th>33</th>
      <td>67</td>
      <td>Celeste, Incarnation of the Corrupted</td>
      <td>4.0</td>
      <td>$2.31</td>
      <td>$9.24</td>
    </tr>
    <tr>
      <th>37</th>
      <td>60</td>
      <td>Wolf</td>
      <td>5.0</td>
      <td>$1.84</td>
      <td>$9.20</td>
    </tr>
    <tr>
      <th>42</th>
      <td>1</td>
      <td>Crucifer</td>
      <td>4.0</td>
      <td>$2.28</td>
      <td>$9.12</td>
    </tr>
    <tr>
      <th>46</th>
      <td>150</td>
      <td>Deathraze</td>
      <td>2.0</td>
      <td>$4.54</td>
      <td>$9.08</td>
    </tr>
  </tbody>
</table>
</div>




```python
#As final considerations:
# • Your script must work for both data-sets given.
# • You must use the Pandas Library and the Jupyter Notebook.
# • You must submit a link to your Jupyter Notebook with the viewable Data Frames.
# • You must include an exported markdown version of your Notebook called README.md in your GitHub repository.
# • You must include a written description of three observable trends based on the data.
# • See Example Solution for a reference on expected format.

```
