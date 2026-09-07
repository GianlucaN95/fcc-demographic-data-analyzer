import pandas as pd

def calculate_demographic_data(print_data=True):
    # 1. Legge il database del censimento fornito da freeCodeCamp
    df = pd.read_csv("adult.data.csv")

    # 2. Conta quanti elementi ci sono per ogni etnia (race)
    race_count = df['race'].value_counts()

    # 3. Calcola l'età media degli uomini
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 4. Calcola la percentuale di persone con una laurea (Bachelors)
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 5. Divide la popolazione in base all'istruzione alta (laurea, master, dottorato) o bassa
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # 6. Calcola le percentuali di chi guadagna più di 50K in base al livello di studio
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').mean() * 100, 1)

    # 7. Trova il numero minimo di ore lavorate a settimana
    min_work_hours = df['hours-per-week'].min()

    # 8. Trova la percentuale di chi lavora il minimo delle ore ma guadagna comunque più di 50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    # 9. Trova lo stato con la percentuale più alta di persone ricche (>50K)
    country_stats = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack() * 100
    highest_earning_country = country_stats['>50K'].idxmax()
    highest_earning_country_percentage = round(country_stats['>50K'].max(), 1)

    # 10. Trova l'occupazione più comune per chi è ricco in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # Confeziona tutti i risultati per il test automatico
    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors: {percentage_bachelors}%")

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
