def analyze_beam(L, W1, W2, x):
    #Max reactions at A and B:
    R_A_max= (W1*L + W2*(L-x))/L #Rxn increases at A as W1 comes closer to A (so for max rxn at A, W1 should be at A)
    R_B_max= (W1*(L-x) + W2*L)/L

    #-------------------------------------------------------------------------
    #For W1 at 0 metre (i.e. W1 at A), BM_01 and SF_01 at 0.5L:

    R_A= (W1*L + W2*(L-x))/L #R_A in this case (which is equal to R_A_max)
    if (x<=0.5*L):
        BM_01= R_A*0.5*L - (W1*0.5*L + W2*(0.5*L-x))
        SF_01= R_A - (W1+W2)
    else:
        BM_01= R_A*0.5*L - W1*0.5*L
        SF_01= R_A-W1

    #-------------------------------------------------------------------------
    #Max BM and SF:

    #Max BM occurs at mid-point, i.e. at L/2 when both loads W1 and W2 are placed symmetrically about the mid-point
    #Max SF occurs at either point A or B depending on whether R_A_max>R_B_max or R_B_max>R_A_max
    #Max SF will occur at both points A and B if R_A_max=R_B_max

    BM_max=(W1+W2)*(L-x)/4
    SF_max=max(R_A_max, R_B_max)

    loc_BM_max= L/2
    loc_SF_max_1= 0
    loc_SF_max_2=None #when R_A_max=R_B_max, two locations of SF_max will exist
    if (R_B_max>R_A_max):
        loc_SF_max_1= L
    elif (R_A_max==R_B_max): #if (R_A_max=R_B_max)
        loc_SF_max_1= 0
        loc_SF_max_2= L 

    output= {
        "Max Reaction at A (kN)": R_A_max,
        "Max Reaction at B (kN)": R_B_max,
        "BM_01 (in kN-m)": BM_01,
        "SF_01 (in kN)": SF_01,
        "Location of BM_max from A (in metres)": loc_BM_max,
        "Location of SF_max from A (in metres)": loc_SF_max_1,
        "Location of SF_max_2 from A (in metres)": loc_SF_max_2
    }
    
    return output



if __name__ == "__main__":
    L=float(input("Enter the length of the beam (in metres): "))
    W1=float(input("Enter the value of load W1 (in kN): "))
    W2=float(input("Enter the value of load W2 (in kN): "))
    x=float(input("Enter distance x between W1 and W2 (in metres): "))

    output=analyze_beam(L, W1, W2, x)

    for key, value in output.items():
        if (value!=None):
            print(f"{key}: {value:.3f}")

