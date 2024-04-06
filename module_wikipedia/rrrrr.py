# # Open the text file in read mode
# with open("CovidNewsTxt/countries/Australia_(January%E2%80%93June.txt", "r") as file:
#     # Initialize a list to store covidnews
#     covidnews = []
    
#     # Initialize a variable to store the current paragraph
#     paragraph = ""
    
#     # Read the file line by line
#     for line in file:
#         # If the line is not empty, append it to the current paragraph
#         if line.strip():
#             paragraph += line
#         # If the line is empty and current paragraph is not empty, 
#         # append the current paragraph to the list of covidnews
#         elif paragraph:
#             covidnews.append(paragraph.strip())
#             paragraph = ""
    
#     # Append the last paragraph if any
#     if paragraph:
#         covidnews.append(paragraph.strip())

# # # Print the covidnews
# # for i, paragraph in enumerate(covidnews, start=1):
# #     print(f"Paragraph {i}:")
# #     print(paragraph)
# #     print()
# print(covidnews)








covidnews = ["February 2020::6 February – A third case of coronavirus is confirmed in the UK. 10 February – The total number of cases in the UK reaches eight as four further cases are confirmed in people linked to an affected man from Brighton. 11 February – A ninth case is confirmed in London. 23 February – The  DHSC  confirms a total of 13 cases in the UK as four new cases in passengers on the cruise ship  Diamond Princess  are detected. They are transferred to hospitals in the UK. 28 February – The first British death from the disease is confirmed by the  Japanese Health Ministry ; a man  quarantined  on the  Diamond Princess  cruise ship. 29 February - The BBC reports the first case of a man in  Surrey  to be infected with COVID-19 whilst in the UK who had not recently travelled abroad.","March 2020::5 March – The first death from coronavirus in the UK is confirmed,  as the number of cases exceeds 100, with a total of 115 having tested positive. England's  Chief Medical Officer ,  Chris Whitty , tells MPs that the UK has now moved to the second stage of dealing with COVID-19 – from  containment  to the  delay  phase. 8 March – A third death from coronavirus is reported, at  North Manchester General Hospital , as the number of cases in the UK reaches 273, the largest single-day increase so far. Manchester United  played against  Manchester City  at  Old Trafford  with 73,288 spectators.  The match was later estimated to have caused 27 additional COVID deaths. 10-13 March -  Cheltenham Festival  begins its multiple day event with more than 250,000 attending. The event ended on 13 March. Many blame the event for spreading COVID-19 and the BBC reports  Gloucestershire County Council says any investigation should be led at a national level .  The event was estimated to have caused 37 additional COVID deaths, while several of the sporting events also caused thousands of infections. 11 March – The  Bank of England  cuts its baseline interest rate from 0.75  to 0.25 , back down to the lowest level in history. The  Liverpool FC vs. Atletico Madrid football match  was played at  Anfield  with 3,000 Madrid fans among the 52,000 spectators, some of whom visited bars after the match. The match was later estimated to have added 41 deaths by COVID-19. 12 March –  Public Health England  stops performing  contact tracing , as widespread infections overwhelm capacity. 13 March – The  Premier League   2019–2020 season  is suspended, amid a growing list of worldwide sporting cancellations and postponements due to COVID-19. Elections including the  English local elections ,  London mayoral election  and  police and crime commissioner elections , scheduled for May 2020, are postponed for a year because of the coronavirus. 17 March – NHS England announces that from 15 April all non-urgent operations in England will be postponed, to free up 30,000 beds to help tackle the virus. 20 March – Northwick Park Hospital  in  Harrow  declares a  critical incident  due to a surge in patients with coronavirus. Prime Minister Boris Johnson  orders all cafes, pubs and restaurants to close  from the evening of 20 March, except for take-away food, to tackle coronavirus. All the UK's nightclubs, theatres, cinemas, gyms and leisure centres are told to close  as soon as they reasonably can ."]






# import re


# months = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06',
#                'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}

# covidnews = ["January 2020::On 23 January,  biosecurity officials  began screening arrivals on flights from  Wuhan  to Sydney. Passengers were given an information sheet and asked to present themselves if they had a fever or suspect they might have the disease. On 25 January, the first case of a  SARS-CoV-2  infection was reported, that of a Chinese citizen who arrived from  Guangzhou  on 19 January. On i 26 pm hts. On 25 January The patient was tested and received treatment in  Melbourne .  On the same day, three other patients tested positive in  Sydney  after returning from  Wuhan . Nine cases were recorded in January. From 31 January, foreign nationals returning from China were required to have spent a fortnight in a third country before being allowed into Australia.", "February 2020::By 6 February, three returning members from a tour group in Wuhan were identified in Queensland. Twenty-four Australians were infected on the  Diamond Princess  cruise ship with eight being sent to  Darwin  for two weeks of quarantine.  The number repatriated from the ship are included in the state totals as follows: Qld (3), SA (1), Vic (4), WA (2, one of whom died on 1 March). On 27 February, the prime minister activated the Australian Health Sector Emergency Response Plan for Novel Coronavirus (COVID-19),  stating that the rapid spread of the virus outside of China had prompted the government to elevate its response. On 29 February, after a Queensland case of an infected person returning to Australia from Iran, the government extended the enforced quarantine to people who had been in Iran, requiring them to spend a fortnight in a third country before being allowed into Australia.  There were 14 new cases in February, bringing the number of cases to 23."]

# # covidnews = [
# #     "March 2020::Week 1 edit On 1 March, Australia reported the first death from COVID-19 : a 78-year-old Perth man, who was one of the passengers from Diamond Princess , and who had been evacuated and was being treated in Western Australia . On 2 March, four new cases were reported, two of which were the first cases of community transmission of the virus. These two cases were acquired in Australia whereas all other previous cases were imported from another country. The two cases were in New South Wales: one was acquired from a close relative and the other was a health care worker in Western Sydney. Another confirmed case on this day was a 40-year-old man from Launceston who came back on 29 February from a flight which left Melbourne and landed in Launceston on the same day. He was treated at the Launceston General Hospital as he became the first COVID-19 case in Tasmania . On 4 March, a second death was reported, a 95-year-old woman dying at a Sydney aged-care facility. Main article: Jenny Mikakos Handling of the COVID-19 pandemic On 7 March, Victorian Health Minister Jenny Mikakos confirmed during a press conference that a doctor in Victoria had tested positive for COVID-19. The doctor in his 70s had returned to Australia from the United States on 29 February. From 2 to 6 March, the doctor had consulted approximately 70 patients at The Toorak Clinic in Melbourne and two patients at an aged-care facility. The clinic was closed over the weekend and patients were contacted to self-isolate. Health officials sought to notify passengers on the doctor's flights. The doctor believed he only had a mild cold and was fit to return to work, hitting back at the minister for her comments. Week 2 edit On 8 March, an 82-year-old man died, becoming the second death at the Dorothy Henderson Lodge aged-care facility and the third death in the country. On 9 March, the principal of Carey Baptist Grammar confirmed that one of the teachers at their Kew campus was infected with the virus. This teacher, a woman in her 50s, was confirmed to be the partner of an individual who was on the same flight from the US that the general practitioner (GP) of Toorak Clinic was on. On 11 March, the head of the Museum of Old and New Art (MONA), David Walsh, cancelled the MONA FOMA winter arts festival Dark Mofo . In a statement, David Walsh stated I know that the cancellation will murder an already massacred tourism environment, but I feel like I have no choice. On 12 March, the ACT announced its first case, the 142nd case in Australia. A man in his 30s had not travelled overseas but did travel outside of the ACT. Actor Tom Hanks and his wife Rita Wilson advised that they had tested positive and were in isolation. Later that day, an initial 17.6 billion stimulus package was unveiled by the Prime Minister to protect Australians' health, secure jobs and set the economy to bounce back from the crisis. West Australian health minister Roger Cook has informed the public that the Western Australian Department of health is postponing upgrades at Peel Health Campus to accommodate patients with the virus. There were concerns that the upgrade would temporarily halve the Emergency Department (ED) waiting room capacity, preventing isolation of ED patients from patients with the virus. The upgrade has been postponed to 1 October 2020. Victoria confirmed nine new cases, one of which was the first case of human-to-human transmission in the state. A McLaren Formula One team member on the now-cancelled Australian Grand Prix tested positive for the virus. This brought the Victorian total to 36 and the national total to 175. The Victorian government declared they are suspending all jury trials to limit the spread of the virus. Home Affairs Minister Peter Dutton tested positive in Queensland on 13 March. Week 3 edit On 10 March, Victorian Premier Daniel Andrews warned Victorians to expect extreme measures in the wake of the federal government updating the travel advice for Italy. These could include cancelling major sporting events, requiring entire economic sectors to work from home, and calling recently retired health professionals to return to work. On 16 March, Victorian Premier Daniel Andrews declared a state of emergency until 13 April. The State of Emergency was subsequently extended (see below). Also on 16 March, the 2020 National Folk Festival in Canberra was cancelled. The University of Queensland stopped all teaching for the week after three students tested positive for the virus. Western Australia introduced similar measures as New South Wales, preventing schools from organising gatherings of over 500. Susan McDonald, a Queensland senator, confirmed being infected with the virus. New South Wales Liberal senator, Andrew Bragg, was the third Australian politician to test positive. On 17 March, the New South Wales government announced a A 2.3 billion stimulus package, including A 700 million for health services. A 450 million was allocated to waive payroll tax for 3 covidnews. A 250 million so state-owned buildings and public schools could employ more cleaners. A 750 million was allocated for capital works and public asset maintenance. On 18 March, a human biosecurity emergency was declared by the Governor-General of Australia, David Hurley, under Section 475 of the Biosecurity Act 2015 . Also on 18 March, the cruise ship Ovation of the Seas docked in Sydney and discharged about 3,500 passengers. 79 passengers had tested positive for the virus by 1 April. Voyager of the Seas also docked that day. By 2 April, 34 passengers and 5 crew members had tested positive for the virus in New South Wales alone. Still on 18 March, the Northern Territory government announced an economic stimulus package of A 60 million. On 18 March in Tasmania the Agfest agricultural field day , set for 7–9 May, was cancelled and replaced by an online event that ran from 7–28 May, On 19 March, Celebrity Solstice docked and contributed a further 11 cases to NSW figures by 2 April. On the same day, the cruise ship Ruby Princess discharged 2,700 passengers in Sydney. It was announced on 20 March that three of 13 passengers had tested positive for the coronavirus. New South Wales health authorities asked all passengers to go into self-isolation. Also on 19 March, Qantas confirmed it would suspend about 60 of domestic flights, put two-thirds of its employees on leave, suspend all international flights and ground more than 150 of its aircraft from the end of March until at least 31 May 2020 following expanded government travel restrictions in response to COVID-19 . On 22 March the federal government announced a second stimulus package of A 66 billion, increasing the amount of total financial package offered to A 89 billion. This included several new measures; most notably a Coronavirus Supplement of an extra A 550 per fortnight of income support, relaxed eligibility criteria for individuals on Jobseeker Payment (formerly Newstart), and grants of up to A 100,000 for small and medium-sized businesses. Week 4 edit On 24 March, one passenger from Ruby Princess had died and 133 on the ship had tested positive. On 28 March 284 passengers had tested positive. On 25 March, the National COVID-19 Coordination Commission (NCCC) was established by the Prime Minister, as a strategic advisory body for the national response to the pandemic. The NCCC's role includes providing advice on public-private partnerships and coordination to mitigate the social and economic impacts of the pandemic. From 12 pm on this day, Australia required that Australian citizens and permanent residents seek exemptions to leave the country. On 27 July, the Prime Minister renamed the NCCC, to the National COVID-19 Commission Advisory Board (NCC) to better reflect the advisory nature of the body. Week 5 edit The cruise ship Artania docked at Fremantle on 27 March. Most of the 850 passengers flew home from Perth to Germany on 28–29 March. 41 passengers and crew tested positive to COVID-19 and were being treated in Perth hospitals. When the cruise departed on 18 April 79 of Western Australia's 541 cases were passengers and crew off the Artania with one death acknowledged as being a crew member from the Philippines. As of 30 March, at least 440 passengers (211 in New South Wales, 71 in South Australia, 70 in Queensland, 43 in Western Australia, 22 in the Australian Capital Territory, 18 in Victoria, three in Tasmania and two in the Northern Territory) from Ruby Princess had tested positive for the virus. As of 31 March 2020, five of them had died, one in the Australian Capital Territory, two in Tasmania, one in New South Wales and one in Queensland. The same day, the Australian Government announced its largest economic support package in response to the crisis, a 130 billion JobKeeper wage subsidy program. This figure was later revised to 70 billion when an error of estimation came to light. The JobKeeper program would pay employers up to 1500 a fortnight per full-time, part-time or casual employee that has worked for that business for over a year, if the business fits criteria involving a loss of turnover as a result of the pandemic. On the evening of 31 March, six baggage handlers from Adelaide Airport had tested positive. As a result, up to 100 other staff from the airport were required to self-isolate, causing cancellations of flights to and from Adelaide. ",
# #     "April 2020::On 1 April, the Western Australian State Government introduced intrastate travel restriction, limiting movements between the regions of Western Australia . On 2 April, the number of cases in Victoria exceeded 1,000, including over 100 healthcare workers. Also on 2 April, the Federal government announced the temporary provision of free childcare so that people could continue working, and to prevent closure of childcare centres. The Government will pay half each centre's operating costs. The free childcare ended on 12 July, and the previous Child Care Subsidy was reintroduced. On 5 April, New South Wales Police Force launched a criminal investigation into whether the operator of Ruby Princess , Carnival Australia , broke the Biosecurity Act 2015 (Cwth) and New South Wales state laws, by deliberately concealing COVID-19 cases. On 5 April, the Queen of Australia addressed the Commonwealth in a televised broadcast, in which she asked people to take comfort that while we may have more still to endure, better days will return . She added, we will be with our friends again; we will be with our families again; we will meet again . On 6 April, the Department of Health revealed that 2,432 people recovered from the infection as the federal government started reporting recovery statistics. This is more than a third from the official number reported so far, Deputy Chief Medical Officer Professor Paul Kelly stating, I think it is important. Firstly it really reinforces that message, which is a true one, that most people who get this disease do recover . The day before, at 3 pm, it was announced that 2,315 of the 5,687 confirmed coronavirus cases had recovered. On 11 April, the charity Anglicare was advised of an outbreak at its Newmarch House aged care nursing home in Caddens, New South Wales . On 14 April, the outbreak was linked to an infected staff member with minor symptoms, but who attended work for six shifts. Ten residents and five other staff tested positive for coronavirus. On 27 and 28 April, four residents of the home died in less than 24 hours, bringing to eleven the number of residents who had died from COVID-19 since 11 April. By 9 May, there had been 69 COVID-19 cases linked to the facility, 32 staff and 37 residents. On 19 May, the 19th resident died from coronavirus. Also on 11 April, the South Australian state government announced its own A 350 million COVID-19 related economic stimulus measures. On 13 April, the Tasmanian government closed the North West Regional Hospital and North West Private Hospital for cleaning, and put the entire staff of over 1,000 people and their families into quarantine. On 14 April the Federal government announced the COVIDSafe digital contact tracing app. On 15 April, a Western Australian man became the first person in Australia to be jailed for breaking a self-isolation directive. On 27 April, the Federal government announced A 94.6 million of support was available for zoos, wildlife parks and aquariums in financial difficulties due to coronavirus restrictions. On 30 April 2020, the ACT declared itself to be free of all known cases of COVID-19, the first Australian jurisdiction. However, on 4 May there was a one new case, a young woman who acquired the virus overseas. On 10 May, the ACT was again free of active COVID-19 cases."
# # ]

# # #  consider some cases : 
# #     1. handle the cases with same date example 25 January "On 25 January, the first case of a  SARS-CoV-2  infection was reported, that of a Chinese citizen who arrived from  Guangzhou  on 19 January. By 26 pm hts. On 25 January The patient was tested and received treatment in  Melbourne ."
# #     2. for this case "By 26 pm hts." , it should be consider in the prevoius date data.


# # def fetch_data_date_wise(covidnews):
# #     for month_data in covidnews:
# #         month, data = month_data.split("::")
# #         print(f"\nMonth: {month}")

# #         # Use regular expression to find dates
# #         date_pattern = r"(On|By|From) (\d{1,2} \w+)"
# #         dates = re.findall(date_pattern, data)

# #         for date in dates:
# #             date_prefix, date_str = date
# #             # Find the data corresponding to the date
# #             start_index = data.index(date_prefix + " " + date_str)
# #             next_date_pattern = r"(On|By|From) (\d{1,2} \w+)"
# #             next_date_match = re.search(next_date_pattern, data[start_index + 1:])
# #             if next_date_match:
# #                 end_index = start_index + next_date_match.start()
# #             else:
# #                 end_index = len(data)
# #             date_data = data[start_index:end_index]

# #             # Check for additional information after the first date
# #             additional_info_start = date_data.find(". On")
# #             if additional_info_start != -1:
# #                 additional_info = date_data[additional_info_start + 2:]
# #                 date_data = date_data[:additional_info_start + 2] + "\n" + additional_info

# #             print(f"\nDate: {date_str}")
# #             print(date_data)

# # fetch_data_date_wise(covidnews)

# def fetch_data_date_wise(covidnews):
#     for month_data in covidnews:
#         month_name, data = month_data.split("::")
#         # print(f"\nMonth: {month_name}")

#         # Use regular expression to find dates
#         date_pattern = r"(On|By|From) (\d{1,2}) (\w+)"
#         dates = re.findall(date_pattern, data)

#         for date in dates:
#             date_prefix, day, month = date
#             month_num = months.get(month.capitalize(), None)
#             if month_num:
#                 date_str = f"{day} {month}"
#                 # Find the data corresponding to the date
#                 start_index = data.index(date_prefix + " " + date_str)
#                 next_date_pattern = r"(On|By|From) (\d{1,2}) (\w+)"
#                 next_date_match = re.search(next_date_pattern, data[start_index + 1:])
#                 if next_date_match:
#                     end_index = start_index + next_date_match.start()
#                 else:
#                     end_index = len(data)
#                 date_data = data[start_index:end_index]

#                 # Check for additional information after the first date
#                 additional_info_start = date_data.find(". On")
#                 if additional_info_start != -1:
#                     additional_info = date_data[additional_info_start + 2:]
#                     date_data = date_data[:additional_info_start + 2] + "" + additional_info

#                 # Split the input into day and month
#                 d, m = date_str.split()
#                 # Convert the date into two-digit format
#                 t = d.zfill(2)
#                 formatted_date = f"{t} {m}"

#                 print(f"{formatted_date}::{date_data}\n")
#                 # print(f"\nDate: {date_str}")
#                 # print(date_data)
#                 # return

# fetch_data_date_wise(covidnews)



