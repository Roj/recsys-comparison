//evaluate(new File("algorithms/parameters/useruser.groovy"))
import org.lenskit.baseline.BaselineScorer
import org.lenskit.baseline.UserMeanBaseline
import org.lenskit.baseline.UserMeanItemScorer
import org.lenskit.baseline.ItemMeanRatingItemScorer

import org.lenskit.knn.user.UserUserItemScorer

import org.lenskit.transform.normalize.VectorNormalizer
import org.lenskit.transform.normalize.UserVectorNormalizer
import org.lenskit.transform.normalize.MeanCenteringVectorNormalizer

import org.lenskit.knn.NeighborhoodSize

bind ItemScorer to UserUserItemScorer
// use item-user mean when user-user fails
bind (BaselineScorer,ItemScorer) to UserMeanItemScorer
bind (UserMeanBaseline,ItemScorer) to ItemMeanRatingItemScorer
// normalize by subtracting the user's mean rating
within (UserVectorNormalizer) {
    // for normalization, just center on user means
    bind VectorNormalizer to MeanCenteringVectorNormalizer
}
//load parameters
int nbsize = new File("algorithms/parameters/user-user_neighborhood.txt").text.toInteger()

set NeighborhoodSize to nbsize


