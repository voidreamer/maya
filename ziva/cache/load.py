import maya.mel as mm
import maya.cmds as mc


mc.currentTime( 78 )

for i in xrange( 78,207 ): 
    path = '/work/21729_MOTH/sequences/5000/0560/cloth/jackhammer_acportillo/zCache/v8_skin.%04i.zCache' % i
    mm.eval('zCache -load "%s" jackHammer:skin_zSolverCache;' % path )
