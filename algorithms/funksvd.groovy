import org.lenskit.mf.funksvd.FunkSVDItemScorer
import org.lenskit.mf.funksvd.FeatureCount
import org.lenskit.baseline.ItemMeanRatingItemScorer
import org.lenskit.baseline.BaselineScorer
import org.lenskit.baseline.UserMeanItemScorer
import org.lenskit.baseline.UserMeanBaseline
//import org.lenskit.iterative.IterationCount
import org.grouplens.lenskit.iterative.IterationCount


bind ItemScorer to FunkSVDItemScorer

bind (BaselineScorer, ItemScorer) to UserMeanItemScorer
bind (UserMeanBaseline,ItemScorer) to ItemMeanRatingItemScorer

set FeatureCount to 25
set IterationCount to 125
