import maya.mel as mm
import maya.cmds as mc

for i in xrange( 78,207 ): 
    mc.currentTime( i )
    path = '/work/21729_MOTH/sequences/5000/0560/cloth/jackhammer_acportillo/zCache/v8_skin.%04i.zCache' % i
    mm.eval('zCache -save "%s" jackHammer:skin_zSolverCache;' % path )
    mm.eval('zCache -clear jackHammer:skin_zSolverCache; ' )
