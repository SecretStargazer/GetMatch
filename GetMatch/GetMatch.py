import GetMatchOfNBA
import GetMatchOfCBA
import PrintResult


nbaResult = GetMatchOfNBA.getMatch()
PrintResult.printMatch(nbaResult)
cbaResult = GetMatchOfCBA.getMatch()
PrintResult.printMatch(cbaResult)