// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract evchain{
uint public vcount = 0;
mapping(uint => evdetails) public ev;
struct evdetails{
	uint bid;
	uint centerid;
	string centername;
	string phone;
	string email;
	string latitude;
	string longitude;
	string place;
}
uint public vcount1 = 0;
mapping(uint => purchasedetails) public pdetails;
struct purchasedetails{
	uint bid;
	uint payid; 
	uint bookingid;
	string amount;
	string paydate;
}

function add_info(uint _bid,uint _centerid,string memory _centername,string memory _phone,string memory _email,string memory _latitude,string memory _longitude,string memory _place)public{
        vcount++;
     	ev[vcount]=evdetails(_bid,_centerid,_centername,_phone,_email,_latitude,_longitude,_place);
    }

function add_purchase_info(uint _bid,uint _payid,uint _bookingid,string memory _amount,string memory _paydate)public{
        vcount1++;
     pdetails[vcount1]=purchasedetails(_bid,_payid,_bookingid,_amount,_paydate);
    }

}