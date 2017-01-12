def main():

    prior = 0.5
    tony = {"Appearance": 0.5, "Intelligence": 0.3, "Personality": 0.2}
    jake = {"Appearance": 0.3, "Intelligence": 0.5, "Personality": 0.2}

    total_probability = (tony["Intelligence"] * tony["Personality"] * prior) + (jake["Intelligence"] * tony["Personality"] * prior)

    print(total_probability)

    tony_posterior_probability = (tony["Intelligence"] * tony["Personality"] * prior) / total_probability
    jake_posterior_probability = (jake["Intelligence"] * jake["Personality"] * prior) / total_probability

    print("Tony's Posterior Probability: ", tony_posterior_probability)
    print("Jake's Posterior Probability: ", jake_posterior_probability)


if __name__=="__main__":
    main()
