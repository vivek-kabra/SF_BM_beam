def analyze_beam(L, W1, W2, x):
    #Max reactions at A and B:
    R_A_max= (W1*L + W2*(L-x))/L #Rxn increases at A as W1 comes closer to A (so for max rxn at A, W1 should be at A)
    R_B_max= (W1*(L-x) + W2*L)/L

    #-------------------------------------------------------------------------

    output= {
        "Max Reaction at A (kN)": R_A_max,
        "Max Reaction at B (kN)": R_B_max
    }
    
    return output



if __name__ == "__main__":
    L=float(input("Enter the length of the beam (in metres): "))
    W1=float(input("Enter the value of load W1 (in kN): "))
    W2=float(input("Enter the value of load W2 (in kN): "))
    x=float(input("Enter distance x between W1 and W2 (in metres): "))

    output=analyze_beam(L, W1, W2, x)

    for key, value in output.items():
        print(f"{key}: {value:.3f}")

