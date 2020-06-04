import random

fn_str = "blanket, bullet, biscuit, biggest, breakfast, ballet, banquet, basket, blackout, bandit, Bharat, Baptist,\
 bouquet, bisect, blatant, Belfast, beaut, boycott, Bigfoot, Bennett, ballast, beret, bonnet, bereft, bullshit, ballot,\
  bayonet, buffet, beget, bracket, barest, braggart, burnout, beignet, bequest, bobcat, beetroot, boggart,\
   backseat, Bogart, booklet, blacklist, bigot, blowout, blueprint, bedpost, basalt, Buddhist, brisket, becket,\
    bearcat, Belmont, behest, benight, breakout, ballpoint, babbitt, billet, brocket, breadfruit, backrest, Binet,\
     Benet, brownout, buffett, backset, bombast, bedrest, bouffant, barbet, Bridgeport, briquet, bezant, beset,\
      bullfight, Beirut, buret, bomblet, birthright, bloodlust, beachfront, brevet, bratwurst, befit, buckshot,\
       Blackfoot, bypast, byzant, buckwheat, broadsheet, backbeat, bedsit, brickbat, burnet, Berit, basset, bartlett,\
        bailment, brunet, bemist, Bradstreet, Burnett, bidet, bifrost, bedsheet, barblet, bepaint, betwixt, besot,\
         brooklet, bombsight, bankrupt, bedfast, brisant, barghest, backchat, beechnut, Brigit, burbot, butut, bezzant,\
          beanfeast, bloodthirst, browbeat, birthroot, bedight, Bizet, bluepoint, birdnest, bloodwort, baguet, bespot,\
           breadroot, blackheart, begirt, butat, branchlet, birthwort, backlist, banjoist, breechclout, bosket, bennet,\
            bogmat, bullbat, bacchant, bowknot, bassist"

ln_str = "Jordan, Jason, Julian, Jan, Jackson, Jonathan, john, Johnson, Jefferson, japan, Jain, jean, junction, join,\
 Jamestown, justification, juxtaposition, Jamaican, jurisdiction, Johnston, Justinian, Jamison, Jensen, javelin,\
  jargon, jawan, Jovian, jubilation, jollification, jazzman, jerkin, Javan, Jordanian, jactation, jillion, jettison,\
   Jansen, jaculation, junkman, jellification, Joplin, juryman, Jacobean, Jacobin, jardin, Jonson, jambon, Jolson,\
    johnsonian, Jacksonian"


def main():
    print(
        make_name(
            convert_str_to_list(fn_str),
            convert_str_to_list(ln_str)
        )
    )


def make_name(fn_list, ln_list):
    fn_index = random.randint(0, len(fn_list))
    ln_index = random.randint(0, len(ln_list))
    fn = fn_list[fn_index]
    ln = ln_list[ln_index]
    fn = fn[:1].upper() + fn[1:]
    ln = ln[:1].upper() + ln[1:]
    return fn + " " + ln


def convert_str_to_list(start_str):
    return start_str.replace(" ", "").split(",")


main()