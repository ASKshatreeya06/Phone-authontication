import Aadhar
#import FingerPrint
#import faceRecognition
#import Iris
#import MobileNumber
#import OTP
#import EmailID
import hashlib
import os
import json

def getAadharDetails(aadharNumber):
    aadharDetails={
        MobileNumber: '',
            OTP: '',
            EmailID: '',
            FaceRecognition: '',
            FingerPrint: '',
            Iris: ''
    }
    if aadharDetails is None:
        return None
    
    MobileNumber.getMobileNumber(aadharNumber)
    if MobileNumber is None:
         return None
    elif MobileNumber is not None:
        OTP.getOTP(MobileNumber)
        if OTP is None:
            return None
        elif OTP is not None:
            EmailID.getEmailID(aadharNumber)
            if EmailID is None:
                return None
            elif EmailID is not None:
                faceRecognition.getFaceRecognition(aadharNumber)
                if faceRecognition is None:
                    return None
                elif faceRecognition is not None:
                    FingerPrint.getFingerPrint(aadharNumber)
                    if FingerPrint is None:
                        return None
                    elif FingerPrint is not None:
                        Iris.getIris(aadharNumber)
                        if Iris.getIris is None:
                            return None
                        elif Iris.getIris is not None:
                            return aadharDetails
                        
if __name__=="__main__":
    aadharNumber = int(input("Enter your aadhar number: "))
    aadharDetails = getAadharDetails(aadharNumber)
    if aadharDetails is None:
        print("Aadhar details not found")
    else:
        print("Aadhar details found")
        print(aadharDetails)