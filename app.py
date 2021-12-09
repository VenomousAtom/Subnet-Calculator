from flask import Flask, request, render_template, url_for
import check_entries as ck
import subnet_values as sbv

app = Flask(__name__)

def subnet_values(class_value, ip, cidr):
    
    if class_value == "A":
        result = sbv.networkClassA(ip, cidr)

    elif class_value == "B":
        result = sbv.networkClassB(ip, cidr)

    elif class_value == "C":
        if cidr >= 24 and cidr <= 31:
            result = sbv.networkClassC(ip, cidr)
        elif cidr == 32:
            result = sbv.networkclass32(ip, cidr)

    elif class_value == "Any":
        if cidr < 8:
            result = sbv.networkClassZero(ip, cidr)
        elif cidr >= 8 and cidr <= 15:
            result = sbv.networkClassA(ip, cidr)
        elif cidr >= 16 and cidr <= 23:
            result = sbv.networkClassB(ip, cidr)
        elif cidr >= 24 and cidr <= 32:
            result = sbv.networkClassC(ip, cidr)
        elif cidr == 32:
            result = sbv.networkclass32(ip, cidr)
    
    return result
        

@app.route('/', methods=["GET","POST"])
def home():
    return render_template('index.html')

@app.route('/eval', methods=["GET","POST"])
def eval():
    return render_template('evaluate.html')

@app.route('/result', methods=["GET","POST"])
def result():
    if request.method == "POST":
        class_value = request.form.get("input1")
        print(class_value)
        iprot = request.form.get("input2")
        print(iprot)
        cidr = request.form.get("input3")
        print(cidr)

        if class_value != "Any":
            ip_val = ck.check_ip(class_value,iprot)
            cidr_val = ck.check_cidr(class_value,cidr)
        else:
            ip_val = "VALID"
            cidr_val = "VALID"
        
        if ip_val != "VALID" or cidr_val != "VALID":
            return render_template('index.html', ip_val=ip_val, cidr_val=cidr_val)

        elif ip_val == "VALID" and cidr_val == "VALID":
            
            vals = subnet_values(class_value, iprot, int(cidr))
            
            ip_addr = vals["IP Address"] 
            dfg_ip = vals["Default Gateway IP"]
            ip_ran = vals["Host IP Range"]
            bdc_ip = vals["Broadcast IP"]
            smb = vals["Subnet Mask Binary"]
            smk = vals["Subnet Mask"]
            ci = vals["Cidr"]
            snr = vals["Subnet Ranges"]
            inc = vals["IP Network Class"]
            
            return render_template('result.html', ip_address=ip_addr, def_gate_ip=dfg_ip, ip_range=ip_ran, broadcast_ip=bdc_ip, sub_mask_bin=smb, sub_mask=smk, cidr=ci, net_class=inc, sub_range=snr)



if __name__ == "__main__":
    app.run(debug=True)
