void setup() {
  Serial.begin(9600);
  int t=analogRead(0);

  ADC->ADC_MR |= 0x80; // these lines set free running mode on adc 7 (pin A0)
  ADC->ADC_CR=2;
  ADC->ADC_CHER=0x80;
}

void loop() {
  int t=micros();
  int q=0;
  int a0;
  for(int i=0;i<1000000;i++){
    while((ADC->ADC_ISR & 0x80)==0); // wait for conversion
    a0=ADC->ADC_CDR[7];              // read data
    q+=a0;
  }
  t=micros()-t;
  Serial.print("1 million conversions in ");Serial.print(t);Serial.println(" micros");
}
