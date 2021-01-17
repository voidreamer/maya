import maya.mel as mm
import maya.cmds as mc


mc.currentTime( 78 )

for i in xrange( 78,207 ): 
    path = '/home/tv01d/zCache/v8_skin.%04i.zCache' % i
    mm.eval('zCache -load "%s" char:skin_zSolverCache;' % path )
