import pandas as pd

class ProcessorIP:
    def __init__(self, df1):
        self.df1 = df1
    
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        df = pd.DataFrame()
        
        df["ClaimDuration"] = pd.to_datetime(X["ClaimEndDt"]) - pd.to_datetime(X["ClaimStartDt"])
        df["ClaimDuration"] = df["ClaimDuration"].apply(lambda x:x.days)
        
        df["InscClaimAmtReimbursed"] = X["InscClaimAmtReimbursed"]
        
        df["AttendingPhysician"] = X["AttendingPhysician"]
        
        df["AdmitDiagnosticCategory"] = X["ClmAdmitDiagnosisCode"].apply(self.CDC_to_TDC)
        
        df["MajorDiagnosticCategory"] = X["DiagnosisGroupCode"].apply(self.DRG_to_MDC)
        
        df["PrincipalDiagnosticCategory"] = X["ClmDiagnosisCode_1"].apply(self.CDC_to_TDC)
        
        df["PrincipalProcedureCategory"] = X["ClmProcedureCode_1"].apply(self.CPC_to_PPC)
        
        df["IPAnnualReimbursementAmt"] = X["IPAnnualReimbursementAmt"]

        df["State"] = X["State"]
        
        dict_phy_fre = self.df1.groupby("AttendingPhysician").count()["ClaimID"].to_dict()
        df["AttendingPhysicianFrequency"] = df["AttendingPhysician"].apply(lambda x: dict_phy_fre.get(x,0))
        
        df = df.drop(["AttendingPhysician"], axis=1)
        
        self.df = df
        
        return df

    def fit_transform(self, X, y=None):
        self.fit(X)
        return self.transform(X)
    
    
    def CDC_to_TDC(self,value):
        if pd.isnull(value):return "0"

        # purely numeric
        if value[0] not in ("V","E"):
            # get the first three digit of Claim Diagnosis Code
            first_three_digit = int(value[:3])
            if 1<= first_three_digit <= 9: return "1"
            if 10<= first_three_digit <= 18: return "2"
            if 20<= first_three_digit <= 27: return "3"
            if 30<= first_three_digit <= 41: return "4"
            if 42<= first_three_digit <= 42: return "5"
            if 45<= first_three_digit <= 49: return "6"
            if 50<= first_three_digit <= 59: return "7"
            if 60<= first_three_digit <= 66: return "8"
            if 70<= first_three_digit <= 79: return "9"
            if 80<= first_three_digit <= 88: return "10"
            if 90<= first_three_digit <= 99: return "11"
            if 100<= first_three_digit <= 104: return "12"
            if 110<= first_three_digit <= 118: return "13"
            if 120<= first_three_digit <= 129: return "14"
            if 130<= first_three_digit <= 136: return "15"
            if 137<= first_three_digit <= 139: return "16"
            if 140<= first_three_digit <= 149: return "17"
            if 150<= first_three_digit <= 159: return "18"
            if 160<= first_three_digit <= 165: return "19"
            if 170<= first_three_digit <= 176: return "20"
            if 179<= first_three_digit <= 189: return "21"
            if 190<= first_three_digit <= 199: return "22"
            if 200<= first_three_digit <= 208: return "23"
            if 209<= first_three_digit <= 209: return "24"
            if 210<= first_three_digit <= 229: return "25"
            if 230<= first_three_digit <= 234: return "26"
            if 235<= first_three_digit <= 238: return "27"
            if 239<= first_three_digit <= 239: return "28"
            if 240<= first_three_digit <= 246: return "29"
            if 249<= first_three_digit <= 259: return "30"
            if 260<= first_three_digit <= 269: return "31"
            if 270<= first_three_digit <= 279: return "32"
            if 280<= first_three_digit <= 289: return "33"
            if 290<= first_three_digit <= 294: return "34"
            if 295<= first_three_digit <= 299: return "35"
            if 300<= first_three_digit <= 316: return "36"
            if 317<= first_three_digit <= 319: return "37"
            if 320<= first_three_digit <= 327: return "38"
            if 330<= first_three_digit <= 337: return "39"
            if 338<= first_three_digit <= 338: return "40"
            if 339<= first_three_digit <= 339: return "41"
            if 340<= first_three_digit <= 349: return "42"
            if 350<= first_three_digit <= 359: return "43"
            if 360<= first_three_digit <= 379: return "44"
            if 380<= first_three_digit <= 389: return "45"
            if 390<= first_three_digit <= 392: return "46"
            if 393<= first_three_digit <= 398: return "47"
            if 401<= first_three_digit <= 405: return "48"
            if 410<= first_three_digit <= 414: return "49"
            if 415<= first_three_digit <= 417: return "50"
            if 420<= first_three_digit <= 429: return "51"
            if 430<= first_three_digit <= 438: return "52"
            if 440<= first_three_digit <= 449: return "53"
            if 451<= first_three_digit <= 459: return "54"
            if 460<= first_three_digit <= 466: return "55"
            if 470<= first_three_digit <= 478: return "56"
            if 480<= first_three_digit <= 488: return "57"
            if 490<= first_three_digit <= 496: return "58"
            if 500<= first_three_digit <= 508: return "59"
            if 510<= first_three_digit <= 519: return "60"
            if 520<= first_three_digit <= 529: return "61"
            if 530<= first_three_digit <= 539: return "62"
            if 540<= first_three_digit <= 543: return "63"
            if 550<= first_three_digit <= 553: return "64"
            if 555<= first_three_digit <= 558: return "65"
            if 560<= first_three_digit <= 569: return "66"
            if 570<= first_three_digit <= 579: return "67"
            if 580<= first_three_digit <= 589: return "68"
            if 590<= first_three_digit <= 599: return "69"
            if 600<= first_three_digit <= 608: return "70"
            if 610<= first_three_digit <= 611: return "71"
            if 614<= first_three_digit <= 616: return "72"
            if 617<= first_three_digit <= 629: return "73"
            if 630<= first_three_digit <= 639: return "74"
            if 640<= first_three_digit <= 649: return "75"
            if 650<= first_three_digit <= 659: return "76"
            if 660<= first_three_digit <= 669: return "77"
            if 670<= first_three_digit <= 677: return "78"
            if 678<= first_three_digit <= 679: return "79"
            if 680<= first_three_digit <= 686: return "80"
            if 690<= first_three_digit <= 698: return "81"
            if 700<= first_three_digit <= 709: return "82"
            if 710<= first_three_digit <= 719: return "83"
            if 720<= first_three_digit <= 724: return "84"
            if 725<= first_three_digit <= 729: return "85"
            if 730<= first_three_digit <= 739: return "86"
            if 740<= first_three_digit <= 759: return "87"
            if 760<= first_three_digit <= 763: return "88"
            if 764<= first_three_digit <= 779: return "89"
            if 780<= first_three_digit <= 789: return "90"
            if 790<= first_three_digit <= 796: return "91"
            if 797<= first_three_digit <= 799: return "92"
            if 800<= first_three_digit <= 804: return "93"
            if 805<= first_three_digit <= 809: return "94"
            if 810<= first_three_digit <= 819: return "95"
            if 820<= first_three_digit <= 829: return "96"
            if 830<= first_three_digit <= 839: return "97"
            if 840<= first_three_digit <= 848: return "98"
            if 850<= first_three_digit <= 854: return "99"
            if 860<= first_three_digit <= 869: return "100"
            if 870<= first_three_digit <= 879: return "101"
            if 880<= first_three_digit <= 887: return "102"
            if 890<= first_three_digit <= 897: return "103"
            if 900<= first_three_digit <= 904: return "104"
            if 905<= first_three_digit <= 909: return "105"
            if 910<= first_three_digit <= 919: return "106"
            if 920<= first_three_digit <= 924: return "107"
            if 925<= first_three_digit <= 929: return "108"
            if 930<= first_three_digit <= 939: return "109"
            if 940<= first_three_digit <= 949: return "110"
            if 950<= first_three_digit <= 957: return "111"
            if 958<= first_three_digit <= 959: return "112"
            if 960<= first_three_digit <= 979: return "113"
            if 980<= first_three_digit <= 989: return "114"
            if 990<= first_three_digit <= 995: return "115"
            if 996<= first_three_digit <= 999: return "116"

        # code beginning with E  
        elif value[0] == "E":
            # get the first three digit of Claim Diagnosis Code
            first_three_digit = int(value[1:4])
            if 0<= first_three_digit <= 0: return "133"
            if 1<= first_three_digit <= 30: return "134"
            if 800<= first_three_digit <= 807: return "135"
            if 810<= first_three_digit <= 819: return "136"
            if 820<= first_three_digit <= 825: return "137"
            if 826<= first_three_digit <= 829: return "138"
            if 830<= first_three_digit <= 838: return "139"
            if 840<= first_three_digit <= 845: return "140"
            if 846<= first_three_digit <= 849: return "141"
            if 850<= first_three_digit <= 858: return "142"
            if 860<= first_three_digit <= 869: return "143"
            if 870<= first_three_digit <= 876: return "144"
            if 878<= first_three_digit <= 879: return "145"
            if 880<= first_three_digit <= 888: return "146"
            if 890<= first_three_digit <= 899: return "147"
            if 900<= first_three_digit <= 909: return "148"
            if 910<= first_three_digit <= 915: return "149"
            if 916<= first_three_digit <= 928: return "150"
            if 929<= first_three_digit <= 929: return "151"
            if 930<= first_three_digit <= 949: return "152"
            if 950<= first_three_digit <= 959: return "153"
            if 960<= first_three_digit <= 969: return "154"
            if 970<= first_three_digit <= 978: return "155"
            if 980<= first_three_digit <= 989: return "156"
            if 990<= first_three_digit <= 999: return "157"

        # code beginning with V
        elif value[0] == "V":
            # get the first two digit of Claim Diagnosis Code
            first_two_digit = int(value[1:3])
            if 1 <= first_two_digit <= 9: return "117"
            if 10 <= first_two_digit <= 19: return "118"
            if 20 <= first_two_digit <= 29: return "119"
            if 30 <= first_two_digit <= 39: return "120"
            if 40 <= first_two_digit <= 49: return "121"
            if 50 <= first_two_digit <= 59: return "122"
            if 60 <= first_two_digit <= 69: return "123"
            if 70 <= first_two_digit <= 82: return "124"
            if 83 <= first_two_digit <= 84: return "125"
            if 85 <= first_two_digit <= 85: return "126"
            if 86 <= first_two_digit <= 86: return "127"
            if 87 <= first_two_digit <= 87: return "128"
            if 88 <= first_two_digit <= 88: return "129"
            if 89 <= first_two_digit <= 89: return "130"
            if 90 <= first_two_digit <= 90: return "131"
            if 91 <= first_two_digit <= 91: return "132"
        
        return "999"
    
    def DRG_to_MDC(self,value):
        if value == "OTH": return "99"
        
        numeric_value = int(value)
        
        if numeric_value == 0: return "0"
        if 1 <= numeric_value <= 17: return "1"
        if 20 <= numeric_value <= 103: return "2"
        if 113 <= numeric_value <= 125: return "3"
        if 129 <= numeric_value <= 159: return "4"
        if 163 <= numeric_value <= 208: return "5"
        if 215 <= numeric_value <= 316: return "6"
        if 326 <= numeric_value <= 395: return "7"
        if 405 <= numeric_value <= 446: return "8"
        if 453 <= numeric_value <= 566: return "9"
        if 573 <= numeric_value <= 607: return "10"
        if 614 <= numeric_value <= 645: return "11"
        if 652 <= numeric_value <= 700: return "12"
        if 707 <= numeric_value <= 730: return "13"
        if 734 <= numeric_value <= 761: return "14"
        if 765 <= numeric_value <= 782: return "15"
        if 789 <= numeric_value <= 795: return "16"
        if 799 <= numeric_value <= 816: return "17"
        if 820 <= numeric_value <= 849: return "18"
        if 853 <= numeric_value <= 872: return "19"
        if 876 <= numeric_value <= 887: return "20"
        if 894 <= numeric_value <= 897: return "21"
        if 901 <= numeric_value <= 923: return "22"
        if 927 <= numeric_value <= 935: return "23"
        if 939 <= numeric_value <= 951: return "24"
        if 955 <= numeric_value <= 965: return "25"
        if 969 <= numeric_value <= 977: return "26"
        if 981 <= numeric_value <= 999: return "27"
    
    def CPC_to_PPC(self,value):
    # handle the missing values
        if pd.isnull(value): return "99"

        # the Claim Procedure Code less than 100 must start with "00"
        if value < 100: return "0"

        # get the first two digits of Claim Procedure Code
        first_two_digit = int(str(value)[:2])
        if 1 <= first_two_digit <= 5: return "1"
        if 6 <= first_two_digit <= 7: return "2"
        if 8 <= first_two_digit <= 16: return "3"
        if 17 <= first_two_digit <= 17: return "3A"
        if 18 <= first_two_digit <= 20: return "4"
        if 21 <= first_two_digit <= 29: return "5"
        if 30 <= first_two_digit <= 34: return "6"
        if 35 <= first_two_digit <= 39: return "7"
        if 40 <= first_two_digit <= 41: return "8"
        if 42 <= first_two_digit <= 54: return "9"
        if 55 <= first_two_digit <= 59: return "10"
        if 60 <= first_two_digit <= 64: return "11"
        if 65 <= first_two_digit <= 71: return "12"
        if 72 <= first_two_digit <= 75: return "13"
        if 76 <= first_two_digit <= 84: return "14"
        if 85 <= first_two_digit <= 86: return "15"
        if 87 <= first_two_digit <= 99: return "16"

        return "99"

class ProcessorOP:
    def __init__(self, df1):
        self.df1 = df1
        
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        df = pd.DataFrame()
        
        df = pd.DataFrame()
        
        df["InscClaimAmtReimbursed"] = X["InscClaimAmtReimbursed"]

        df["AttendingPhysician"] = X["AttendingPhysician"]

        df["PrincipalDiagnosticCategory"] = X["ClmDiagnosisCode_1"].apply(self.CDC_to_TDC)
        
        dict_phy_fre = self.df1.groupby("AttendingPhysician").count()["ClaimID"].to_dict()
        df["AttendingPhysicianFrequency"] = df["AttendingPhysician"].apply(lambda x: dict_phy_fre.get(x,0))
        
        df["State"] = X["State"]
        
        df["Race"] = X["Race"]
        
        df = df.drop(["AttendingPhysician"], axis=1)
        
        self.df = df
        
        return df

    def fit_transform(self, X, y=None):
        self.fit(X)
        return self.transform(X)
    
    
    def CDC_to_TDC(self,value):
        if pd.isnull(value):return "0"

        # purely numeric
        if value[0] not in ("V","E"):
            # get the first three digit of Claim Diagnosis Code
            first_three_digit = int(value[:3])
            if 1<= first_three_digit <= 9: return "1"
            if 10<= first_three_digit <= 18: return "2"
            if 20<= first_three_digit <= 27: return "3"
            if 30<= first_three_digit <= 41: return "4"
            if 42<= first_three_digit <= 44: return "5"
            if 45<= first_three_digit <= 49: return "6"
            if 50<= first_three_digit <= 59: return "7"
            if 60<= first_three_digit <= 66: return "8"
            if 70<= first_three_digit <= 79: return "9"
            if 80<= first_three_digit <= 88: return "10"
            if 90<= first_three_digit <= 99: return "11"
            if 100<= first_three_digit <= 104: return "12"
            if 110<= first_three_digit <= 118: return "13"
            if 120<= first_three_digit <= 129: return "14"
            if 130<= first_three_digit <= 136: return "15"
            if 137<= first_three_digit <= 139: return "16"
            if 140<= first_three_digit <= 149: return "17"
            if 150<= first_three_digit <= 159: return "18"
            if 160<= first_three_digit <= 165: return "19"
            if 170<= first_three_digit <= 176: return "20"
            if 179<= first_three_digit <= 189: return "21"
            if 190<= first_three_digit <= 199: return "22"
            if 200<= first_three_digit <= 208: return "23"
            if 209<= first_three_digit <= 209: return "24"
            if 210<= first_three_digit <= 229: return "25"
            if 230<= first_three_digit <= 234: return "26"
            if 235<= first_three_digit <= 238: return "27"
            if 239<= first_three_digit <= 239: return "28"
            if 240<= first_three_digit <= 246: return "29"
            if 249<= first_three_digit <= 259: return "30"
            if 260<= first_three_digit <= 269: return "31"
            if 270<= first_three_digit <= 279: return "32"
            if 280<= first_three_digit <= 289: return "33"
            if 290<= first_three_digit <= 294: return "34"
            if 295<= first_three_digit <= 299: return "35"
            if 300<= first_three_digit <= 316: return "36"
            if 317<= first_three_digit <= 319: return "37"
            if 320<= first_three_digit <= 327: return "38"
            if 330<= first_three_digit <= 337: return "39"
            if 338<= first_three_digit <= 338: return "40"
            if 339<= first_three_digit <= 339: return "41"
            if 340<= first_three_digit <= 349: return "42"
            if 350<= first_three_digit <= 359: return "43"
            if 360<= first_three_digit <= 379: return "44"
            if 380<= first_three_digit <= 389: return "45"
            if 390<= first_three_digit <= 392: return "46"
            if 393<= first_three_digit <= 398: return "47"
            if 401<= first_three_digit <= 405: return "48"
            if 410<= first_three_digit <= 414: return "49"
            if 415<= first_three_digit <= 417: return "50"
            if 420<= first_three_digit <= 429: return "51"
            if 430<= first_three_digit <= 438: return "52"
            if 440<= first_three_digit <= 449: return "53"
            if 451<= first_three_digit <= 459: return "54"
            if 460<= first_three_digit <= 466: return "55"
            if 470<= first_three_digit <= 478: return "56"
            if 480<= first_three_digit <= 488: return "57"
            if 490<= first_three_digit <= 496: return "58"
            if 500<= first_three_digit <= 508: return "59"
            if 510<= first_three_digit <= 519: return "60"
            if 520<= first_three_digit <= 529: return "61"
            if 530<= first_three_digit <= 539: return "62"
            if 540<= first_three_digit <= 543: return "63"
            if 550<= first_three_digit <= 553: return "64"
            if 555<= first_three_digit <= 558: return "65"
            if 560<= first_three_digit <= 569: return "66"
            if 570<= first_three_digit <= 579: return "67"
            if 580<= first_three_digit <= 589: return "68"
            if 590<= first_three_digit <= 599: return "69"
            if 600<= first_three_digit <= 608: return "70"
            if 610<= first_three_digit <= 612: return "71"
            if 614<= first_three_digit <= 616: return "72"
            if 617<= first_three_digit <= 629: return "73"
            if 630<= first_three_digit <= 639: return "74"
            if 640<= first_three_digit <= 649: return "75"
            if 650<= first_three_digit <= 659: return "76"
            if 660<= first_three_digit <= 669: return "77"
            if 670<= first_three_digit <= 677: return "78"
            if 678<= first_three_digit <= 679: return "79"
            if 680<= first_three_digit <= 686: return "80"
            if 690<= first_three_digit <= 698: return "81"
            if 700<= first_three_digit <= 709: return "82"
            if 710<= first_three_digit <= 719: return "83"
            if 720<= first_three_digit <= 724: return "84"
            if 725<= first_three_digit <= 729: return "85"
            if 730<= first_three_digit <= 739: return "86"
            if 740<= first_three_digit <= 759: return "87"
            if 760<= first_three_digit <= 763: return "88"
            if 764<= first_three_digit <= 779: return "89"
            if 780<= first_three_digit <= 789: return "90"
            if 790<= first_three_digit <= 796: return "91"
            if 797<= first_three_digit <= 799: return "92"
            if 800<= first_three_digit <= 804: return "93"
            if 805<= first_three_digit <= 809: return "94"
            if 810<= first_three_digit <= 819: return "95"
            if 820<= first_three_digit <= 829: return "96"
            if 830<= first_three_digit <= 839: return "97"
            if 840<= first_three_digit <= 848: return "98"
            if 850<= first_three_digit <= 854: return "99"
            if 860<= first_three_digit <= 869: return "100"
            if 870<= first_three_digit <= 879: return "101"
            if 880<= first_three_digit <= 887: return "102"
            if 890<= first_three_digit <= 897: return "103"
            if 900<= first_three_digit <= 904: return "104"
            if 905<= first_three_digit <= 909: return "105"
            if 910<= first_three_digit <= 919: return "106"
            if 920<= first_three_digit <= 924: return "107"
            if 925<= first_three_digit <= 929: return "108"
            if 930<= first_three_digit <= 939: return "109"
            if 940<= first_three_digit <= 949: return "110"
            if 950<= first_three_digit <= 957: return "111"
            if 958<= first_three_digit <= 959: return "112"
            if 960<= first_three_digit <= 979: return "113"
            if 980<= first_three_digit <= 989: return "114"
            if 990<= first_three_digit <= 995: return "115"
            if 996<= first_three_digit <= 999: return "116"

        # code beginning with E  
        elif value[0] == "E":
            # get the first three digit of Claim Diagnosis Code
            first_three_digit = int(value[1:4])
            if 0<= first_three_digit <= 0: return "133"
            if 1<= first_three_digit <= 30: return "134"
            if 800<= first_three_digit <= 807: return "135"
            if 810<= first_three_digit <= 819: return "136"
            if 820<= first_three_digit <= 825: return "137"
            if 826<= first_three_digit <= 829: return "138"
            if 830<= first_three_digit <= 838: return "139"
            if 840<= first_three_digit <= 845: return "140"
            if 846<= first_three_digit <= 849: return "141"
            if 850<= first_three_digit <= 858: return "142"
            if 860<= first_three_digit <= 869: return "143"
            if 870<= first_three_digit <= 876: return "144"
            if 878<= first_three_digit <= 879: return "145"
            if 880<= first_three_digit <= 888: return "146"
            if 890<= first_three_digit <= 899: return "147"
            if 900<= first_three_digit <= 909: return "148"
            if 910<= first_three_digit <= 915: return "149"
            if 916<= first_three_digit <= 928: return "150"
            if 929<= first_three_digit <= 929: return "151"
            if 930<= first_three_digit <= 949: return "152"
            if 950<= first_three_digit <= 959: return "153"
            if 960<= first_three_digit <= 969: return "154"
            if 970<= first_three_digit <= 978: return "155"
            if 980<= first_three_digit <= 989: return "156"
            if 990<= first_three_digit <= 999: return "157"

        # code beginning with V
        elif value[0] == "V":
            # get the first two digit of Claim Diagnosis Code
            first_two_digit = int(value[1:3])
            if 1 <= first_two_digit <= 9: return "117"
            if 10 <= first_two_digit <= 19: return "118"
            if 20 <= first_two_digit <= 29: return "119"
            if 30 <= first_two_digit <= 39: return "120"
            if 40 <= first_two_digit <= 49: return "121"
            if 50 <= first_two_digit <= 59: return "122"
            if 60 <= first_two_digit <= 69: return "123"
            if 70 <= first_two_digit <= 82: return "124"
            if 83 <= first_two_digit <= 84: return "125"
            if 85 <= first_two_digit <= 85: return "126"
            if 86 <= first_two_digit <= 86: return "127"
            if 87 <= first_two_digit <= 87: return "128"
            if 88 <= first_two_digit <= 88: return "129"
            if 89 <= first_two_digit <= 89: return "130"
            if 90 <= first_two_digit <= 90: return "131"
            if 91 <= first_two_digit <= 91: return "132"
        
        return "999"