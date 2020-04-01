import maya.mel as mm
import maya.cmds as mc

for i in xrange( 78,207 ): 
    mc.currentTime( i )
    path = '/home/tv01d/zCache/v8_skin.%04i.zCache' % i
    mm.eval('zCache -save "%s" char:skin_zSolverCache;' % path )
    mm.eval('zCache -clear char:skin_zSolverCache; ' )
