// slot_booking.js

    // Get references to the necessary form elements
// const districtSelect = document.getElementById('district');
// const firstPartyIdProofType = document.getElementById('first_party_id_proof');
// const firstPartyIdProofType = document.getElementById('first_party_id_proof');
// const secondPartyIdProofType = document.getElementById('second_party_id_proof');
// const firstPartyIdProofNumber = document.getElementById('first_party_id_proof_number');
// const secondPartyIdProofNumber = document.getElementById('second_party_id_proof_number');
// const registrationOfficeSelect = document.getElementById('registration_office');

    var firstPartyName = document.getElementById("first_party_name");
    var firstPartyIdProofNumber = document.getElementById("first_party_id_proof_number");
    var firstPartyIdProofType = document.getElementById("first_party_id_proof");
    
    var secondPartyName = document.getElementById("second_party_name");
    var secondPartyIdProofType = document.getElementById("second_party_id_proof");
    var secondPartyIdProofNumber = document.getElementById("second_party_id_proof_number");
    
    var date = document.getElementById("date");
    var timeSlot = document.getElementById("timeSlot");
    var districtSelect = document.getElementById("district");
    var registrationOfficeSelect = document.getElementById("registration_office");
    var mobileNumber = document.getElementById("mobile_number");


const districtToRegistrationOffices = {
    Korba: ['Korba', 'Katghora', 'Pali', 'Pali-Manikpur', 'Pal'],
    Raipur: ['Raipur', 'Abhanpur', 'Arang', 'Mana-Camp', 'Naya Raipur', 'Tilda-Newra'],
    Bastar: ['Bastar', 'Kondagaon', 'Kanker', 'Narayanpur', 'Sukma'],
    Bilaspur: ['Bilaspur', 'Bilha', 'Belha', 'Kota', 'Pendra', 'Takhatpur'],
    Bijapur: ['Bijapur', 'Basaguda'],
    Dantewada: ['Dantewada','Geedam'],
    Dhamtari: ['Dhamtari', 'Kurud', 'Nagri'],
    Durg: ['Durg', 'Patan'],
    Gariaband: ['Gariaband', 'Chhura', 'Mainpur'],
    Janjgir_Champa: ['Janjgir-Champa', 'Akaltara', 'Champa', 'Jaijaipur', 'Nawagarh', 'Pamgarh', 'Sakti', 'Shivrinarayan'],
    Jashpur: ['Jashpur', 'Bagicha', 'Kansabel', 'Kunkuri', 'Manora'],
    Kabirdham: ['Kabirdham', 'Bodla', 'Sahaspur-Lohara'],
    Kanker: ['Kanker', 'Antagarh', 'Bhanupratappur', 'Keskal', 'Koyelibeda', 'Narharpur'],
    Kondagaon: ['Kondagaon', 'Makdi'],
    Korea: ['Korea', 'Baikunthpur', 'Bharatpur', 'Sonhat'],
    Mahasamund: ['Mahasamund', 'Basna', 'Pithora', 'Saraipali'],
    Mungeli: ['Mungeli', 'Pathariya'],
    Narayanpur: ['Narayanpur', 'Orchha'],
    Raigarh: ['Raigarh', 'Dharamjaigarh', 'Gharghoda', 'Kharsia', 'Lailunga', 'Sarangarh'],
    Rajnandgaon: ['Rajnandgaon', 'Ambagarh-Chowki', 'Chhuikhadan', 'Dongargaon', 'Dongargarh', 'Khairagarh', 'Manpur', 'Mohla'],
    Sukma: ['Sukma', 'Chhindgarh', 'Konta'],
    Surajpur: ['Surajpur', 'Bhaiyathan', 'Pratappur', 'Ramanujnagar'],
    Balod: ['Balod', 'Dondi', 'Gunderdehi', 'Gurur', 'Daundi', 'Dondilohara'],
    Baloda_Bazar: ['Baloda Bazar', 'Bhatapara', 'Palari', 'Simga'],
    Balrampur: ['Balrampur', 'Ramanujganj', 'Wadrafnagar', 'Samri'],
    Bemetara: ['Bemetara', 'Berla', 'Saja'],
    Kawardha: ['Kawardha', 'Bodla', 'Pandariya', 'Sahaspur-Lohara'],
    Surguja: ['Surguja', 'Ambikapur', 'Bhaiyathan', 'Lakhanpur', 'Lundra', 'Mainpat', 'Odal', 'Sitapur', 'Udaipur']
};


function updateRegistrationOffices() {
    const selectedDistrict = districtSelect.value
    const offices = districtToRegistrationOffices[selectedDistrict] || [];
    

    registrationOfficeSelect.innerHTML = '';
  
    for (const office of offices) {
        const option = document.createElement('option');
        option.value = office;
        option.textContent = office;
        registrationOfficeSelect.appendChild(option);
    }
}


districtSelect.addEventListener('change', updateRegistrationOffices);


updateRegistrationOffices();

function handleFormSubmission() {

    // var timeSlot = ["10:00 AM", "11:00 AM", "12:00 PM", "01:00 PM", "02:00 PM", "03:00 PM", "04:00 PM", "05:00 PM"]

    var confirmationUrl = "/confirmation/";

    window.location.href = confirmationUrl + "?firstPartyName=" + encodeURIComponent(firstPartyName.value) +
                            "&secondPartyName=" + encodeURIComponent(secondPartyName.value) +
                            "&date=" + encodeURIComponent(date.value) +
                            "&timeSlot=" + encodeURIComponent(timeSlot.value) +
                            "&districtSelect=" + encodeURIComponent(districtSelect.value) +
                            "&registrationOfficeSelect=" + encodeURIComponent(registrationOfficeSelect.value) + 
                            "&bookingStatus=Booked Successfully";
}

document.querySelector("form").addEventListener("submit", function (e) {
    e.preventDefault(); 
    handleFormSubmission(); 
});
